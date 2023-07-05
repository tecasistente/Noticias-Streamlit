import streamlit as st
from newscatcher import Newscatcher

def get_news(search_topic):
  try:  
    nyt = Newscatcher(website = 'nytimes.com', topic=search_topic)
    results = nyt.get_news()
    articles = results['articles']
    return articles
  except:
     return []


sidebar=st.sidebar
topic=sidebar.selectbox(
    "What topic to search?", (['tech', 'news', 'business', 'science', 'finance', 'food', 'politics', 'economics', 'travel', 'entertainment', 'music', 'sport', 'world'])
)
sidebar.text("The topic is "+ topic)

#obtener la lista de  noticias
news=get_news(topic)

st.markdown("<h1 style='text-align: center; color: Blue;'>Nytimes News</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: Blue;'>Powered by Newscatcher</p>", unsafe_allow_html=True)

#barra de busqueda
search = st.text_input("Search news")

filtred_news = []
for item in news:
    if search.lower() in item['title'].lower() or search.lower() in item['summary'].lower():
        filtred_news.append(item)

if len(filtred_news)==0:
   st.error("News not found ")


for item in filtred_news:
    st.subheader(item['title'])
    st.write("Date: " +item['published'])
    st.write("Summary: " + item['summary'])
    st.write("Link: " + item['link'])
    st.markdown("---")  # Agregar una línea separadora entre cada noticia

