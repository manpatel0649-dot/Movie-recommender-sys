import streamlit as st
import pickle
import requests as re



def prediction(movie):
    recomend_movies_path=[]
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    lst=[]
    for i in movie_list:
        lst.append(movies['title'][i[0]])
        recomend_movies_path.append(movies['id'][i[0]])
    return lst,recomend_movies_path

def fatch_poster(movie):
    data=re.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie))
    data=data.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']




movies=pickle.load(open("ndf.pkl","rb"))
movies_lst= movies["title"]

similarity=pickle.load(open("similarity.pkl","rb"))




st.title('Movie Recommender')

option = st.selectbox(
    "Which type of movie do you prefer?",
     movies_lst,
)
if st.button('Recommend'):
    st.write("Recommending Movie")

    recommended_movie_names,recommended_movie_posters=prediction(option)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.write('\n\n')
        st.image(fatch_poster(recommended_movie_posters[0]))
    with col2:
        st.text(recommended_movie_names[1])
        st.write('\n\n')
        st.image(fatch_poster(recommended_movie_posters[1]))

    with col3:
        st.text(recommended_movie_names[2])
        st.write('\n\n')
        st.image(fatch_poster(recommended_movie_posters[2]))
    with col4:
        st.text(recommended_movie_names[3])
        st.write('\n\n')
        st.image(fatch_poster(recommended_movie_posters[3]))
    with col5:
        st.text(recommended_movie_names[4])
        st.write('\n\n')
        st.image(fatch_poster(recommended_movie_posters[4]))




