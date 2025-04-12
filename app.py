import streamlit as st
import pickle

movies = pickle.load(open('movie_list.pkl','rb'))
movies_list = movies['Title'].values

similarity = pickle.load(open('similarityy.pkl','rb'))

st.header('Nepali Movie Recommendation System')
selectvalue = st.selectbox('Select Movie from Dropdown',movies_list)

def recommend(movie):
    movie_index = movies[movies['Title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse = True, key = lambda x:x[1])[1:4]
    recommend_movie = []
    recommend_poster = []
    for i in movie_list:
        recommend_movie.append(movies.iloc[i[0]].Title)
        recommend_poster.append(movies.iloc[i[0]].Image)
    return recommend_movie,recommend_poster
    

if st.button('Show Movies'):
    recommend_movie,recommend_poster = recommend(selectvalue)
    cols = st.columns(3)
    for col, url, title in zip(cols, recommend_poster, recommend_movie):
        with col:
            st.image(url, caption=title)
