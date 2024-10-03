# Movie Recommender System

This project is a movie recommender system built using **Streamlit** and **Python**. It allows users to select a movie from a dropdown menu and get recommendations based on similarity with other movies. The system displays the recommended movie titles along with their posters fetched from the TMDB API.

## Features
- **Movie Selection**: Select a movie from the list.
- **Recommendations**: Get five recommended movies based on similarity.
- **Movie Posters**: View the posters of the recommended movies fetched from the TMDB API.

## How to Run the Project

### Clone the repository:
```bash
git clone https://github.com/Passi264/Recommenderformovies.git

#Navigate to the project directory:
cd Recommenderformovies

#Install the required packages:
pip install -r requirements.txt

#Run the Streamlit app:
streamlit run app.py
```
The app will open in your browser. You can select a movie from the dropdown menu and click "Recommend" to see the recommendations.
## Prerequisites
- Python 3.7 or higher
- Install dependencies from requirements.txt using the command pip install -r requirements.txt
## Project Structure
- app.py: The main script that runs the recommender system using Streamlit.
- movies.pkl: Contains the movie data used for recommendations.
- similarity.pkl.gz: Compressed similarity matrix for the movie recommendations.
- requirements.txt: Lists the dependencies needed to run the project.
## API Used
- TMDB API: The Movie Database API is used to fetch the movie posters.
## How to Fetch Movie Posters
Movie posters are fetched dynamically using the TMDB API. You can get your API key from TMDB and update the API key in the script if needed.
## Future Improvements
- Implement genre-based recommendations.
- Add a user rating system for better recommendations.
## Credits
This project uses movie data and the TMDB API to generate and display movie recommendations.
