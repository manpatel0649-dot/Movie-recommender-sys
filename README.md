Movie Recommender System
Context
A content-based movie recommender system built in Python. It suggests similar movies by analyzing metadata such as genre, cast, crew, and keywords, then ranking similarity using cosine similarity. The project includes a Streamlit-based UI for users to pick a movie and instantly view recommended titles with posters fetched from TMDB.
Features

Recommends top 5 similar movies for any selected title
Fetches movie posters via TMDB API
Simple, interactive Streamlit UI

Tech Stack

Python
Pandas, NumPy
Scikit-learn (cosine similarity)
Streamlit
TMDB API

Installation
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
pip install -r requirements.txt
Usage
streamlit run app.py
How It Works

Movie metadata (genres, cast, crew, keywords) is combined into a single "tags" feature.
Text is vectorized using CountVectorizer/TF-IDF.
Cosine similarity is computed between all movies.
Top N similar movies are returned for a selected title.

Project Structure
├── app.py
├── model.pkl
├── movie_dict.pkl
├── requirements.txt
└── README.md
Future Improvements

Add collaborative filtering
User rating-based personalization
Deploy on Heroku/Streamlit Cloud
