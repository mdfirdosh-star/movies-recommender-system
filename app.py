import streamlit as st
import pandas as pd
import pickle
import requests

# ==================================
# PAGE CONFIG
# ==================================
st.set_page_config(
    page_title="🎬 Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# ==================================
# TMDB API KEY
# ==================================
API_KEY = "25e6566bc26aea4e553b719db4b525a9"

# ==================================
# LOAD DATA
# ==================================
@st.cache_data
def load_data():
    movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
    movies = pd.DataFrame(movies_dict)

    similarity = pickle.load(open("similarity.pkl", "rb"))

    return movies, similarity

movies, similarity = load_data()

# ==================================
# FETCH POSTER
# ==================================
def fetch_poster(movie_id):

    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"

        response = requests.get(
            url,
            timeout=10,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        if response.status_code != 200:
            return "https://via.placeholder.com/500x750?text=Poster+Not+Found"

        data = response.json()

        poster_path = data.get("poster_path")

        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"

        return "https://via.placeholder.com/500x750?text=Poster+Not+Found"

    except Exception:
        return "https://via.placeholder.com/500x750?text=Poster+Not+Found"

# ==================================
# RECOMMEND FUNCTION
# ==================================
def recommend(movie):

    movie_index = movies[movies["title"] == movie].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movie_list:

        movie_id = movies.iloc[i[0]]["id"]

        recommended_movies.append(
            movies.iloc[i[0]]["title"]
        )

        recommended_posters.append(
            fetch_poster(movie_id)
        )

    return recommended_movies, recommended_posters

# ==================================
# TITLE
# ==================================
st.title("🎬 Movie Recommendation System")
st.markdown("### Find movies similar to your favorite movie")

# ==================================
# MOVIE SELECTOR
# ==================================
selected_movie_name = st.selectbox(
    "Select a Movie",
    movies["title"].values
)

# ==================================
# RECOMMEND BUTTON
# ==================================
if st.button("🚀 Recommend Movies"):

    with st.spinner("Finding Similar Movies..."):

        names, posters = recommend(selected_movie_name)

        st.subheader("Recommended Movies")

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.image(posters[0])
            st.caption(names[0])

        with col2:
            st.image(posters[1])
            st.caption(names[1])

        with col3:
            st.image(posters[2])
            st.caption(names[2])

        with col4:
            st.image(posters[3])
            st.caption(names[3])

        with col5:
            st.image(posters[4])
            st.caption(names[4])

# ==================================
# SIDEBAR
# ==================================
st.sidebar.title("About")

st.sidebar.info("""
🎬 Movie Recommendation System

Technologies Used:
- Python
- Pandas
- Streamlit
- TMDB API
- Cosine Similarity
- Machine Learning
""")

st.sidebar.success("Built with ❤️ using Streamlit")