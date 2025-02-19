import streamlit as st
import pickle
import pandas as pd
import requests
import os

from dotenv import load_dotenv
load_dotenv()

os.environ["API_KEY"] = os.getenv("API_KEY")

# def fetch_poster(movie_id):
#    api_key = "839b4035c6b9069f2901cc2cbf287fc1"
#    st.write("hi")
#    response=requests.get('https://api.themoviedb.org/3/movie/{}?{}'.format(movie_id,api_key))
#    data=response.json()
#    st.write(data)
#    #link=data['poster_path']
#    #return "http://image.tmdb.org/t/p/w500/"+link


def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True, key=lambda x:x[1])[1:6]
    recommended_movies=[]
    #recommended_movies_posters=[]
    for i in movies_list:
        movie_id=i[0]
        #fetch poster from API
        recommended_movies.append(movies.iloc[i[0]].title)
        #recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies

movie_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movie_dict)
similarity=pickle.load(open('similarity.pkl','rb'))


st.title('Movie Recommender System')
selected_movie_name=st.selectbox('Select your movie',movies['title'].values)

if st.button('Recommend'):
    names=recommend(selected_movie_name)
    col1, col2, col3, col4, col5 =st.columns(5)
    with col1:
        st.write(names[0])
        #st.image(posters[0])
    with col2:
        st.write(names[1])
        #st.image(posters[1])
    with col3:
        st.write(names[2])
        #st.image(posters[2])
    with col4:
        st.write(names[3])
       # st.image(posters[3])
    with col5:
        st.write(names[4])
        #st.image(posters[4])

