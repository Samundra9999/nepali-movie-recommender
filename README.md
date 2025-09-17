# Nepali Movie Recommendation System

The **Nepali Movie Recommendation System** allows users to select a movie from a dropdown list and get a set of similar Nepali movie recommendations. This recommendation is powered by a **cosine similarity-based approach**, where a precomputed similarity matrix is used to find movies that are similar to the selected one.

---

## Tech Stack

- **Python**
- **Streamlit** for the UI
- **Pandas** for data processing
- **Pickle** for saving/loading data
- **BeautifulSoup** & **Selenium** for scraping movie data

---

## Features

- Select a Nepali movie from a dropdown.
- Get top 3 similar movie recommendations.
- Interactive UI powered by Streamlit.

---

## Live Demo
Check out the live Streamlit app [here](https://nepali-movie-recommender-ltqv2whbqqdssvhhpwvfmh.streamlit.app/)

---

## Getting Started

1. Install dependencies:

   Install streamlit, pandas, pickle, beautifulsoup, selenium

2. Run the app:

    streamlit run app.py

## Movie Data Scraping

- **Scraping**: Collects movie titles, roles, date, etc from Nepali movie websites(IMDB) using **BeautifulSoup** and **Selenium**.

- **Saved as**:
  - `movie_list.pkl` – Contains scraped movie data (e.g., titles, tags, etc).
  - `similarity.pkl` – Cosine similarity matrix between movies.

---

## How it Works

1. Select a movie from the dropdown list.
2. Fetch the similarity scores for that movie from `similarity.pkl`.
3. Display the **top 3 most similar movies** as recommendations.

---

## Disclaimer

**This project was created for educational purposes. The data used in the Nepali Movie Recommendation System is limited, as not all movie details could be fetched during the web scraping process. Therefore, the recommendations may not cover the full range of Nepali movies. The system is intended for learning and demonstration only.**
