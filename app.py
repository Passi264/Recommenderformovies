import streamlit as st
import pickle
import pandas as pd
import requests
import gzip
st.title("Movie recommender system")
with open("movies.pkl", "rb") as f:
    movies_dict = pickle.load(f)
# Load the compressed similarity.pkl.gz file
with gzip.open("similarity.pkl.gz", "rb") as f:
    similarity = pickle.load(f)
def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=5354969d4d1f2ffb9ce9fcd6c3afd0aa&language=en-US".format(movie_id))
    data= response.json()
    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]


def recommend(movie):
    movie_index = new_df[new_df["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies=[]
    recommended_movieposters= []
    for i in movies_list:
        moviee_id= new_df.iloc[i[0]].movie_id
        recommended_movies.append((new_df.iloc[i[0]].title))
        recommended_movieposters.append(fetch_poster(moviee_id))
    return recommended_movies,recommended_movieposters
# If you saved the DataFrame as a dictionary, convert it back to a DataFrame
new_df = pd.DataFrame.from_dict(movies_dict)

# Ensure you access the "title" column correctly
movies_list = new_df["title"].values

# Create the select box with movie titles
option = st.selectbox(
    "Select a movie:",
    movies_list
)

if st.button("Recommend"):
    names,posters = recommend(option)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
