import streamlit as st
import requests
from utils import get_news_list, get_summary

st.title("Summary Page")

# Add a loading animation
with st.spinner("Loading news articles..."):
    news_list = get_news_list()
    news_titles = {news['title']: news for news in news_list}

# Create a selectbox with a custom style
st.markdown("""
    <style>
        .stSelectbox {
            font-size: 18px;
            font-weight: bold;
            color: #00698f;
        }
    </style>
""", unsafe_allow_html=True)

selected_title = st.selectbox("Select News Title", list(news_titles.keys()), index=0)

if selected_title:
    news = news_titles[selected_title]
    st.write(news['id'])
    st.write(news['title'])
    st.write(news['body'])
    st.write(f"Link: {news['link']}")
    st.write(f"Date: {news['datetime']}")
    st.write(f"Category: {news['category']}")
    st.write(f"Reporter: {news['reporter']}")
    st.write(f"Publisher: {news['publisher']}")

    # Add a button with a custom style
    st.markdown("""
        <style>
            .stButton {
                font-size: 18px;
                font-weight: bold;
                color: #ffffff;
                border: none;
                border-radius: 5px;
                padding: 10px 20px;
                cursor: pointer;
            }
        </style>
    """, unsafe_allow_html=True)

    # col1, col2, col3 = st.columns([0, 3, 0])
    # with col2:
    if st.button("Generate Summary", type='primary'):
        with st.spinner("Generating summary..."):
            summary = get_summary(news['id'])
            st.write("Summary:")
            st.write(summary['summary_text'])
            st.balloons()
            st.success("Summary generated successfully!")

# Add a footer with the author section
st.markdown("""
    <style>
        .footer {
            text-align: center;
            color: #808080;
            font-size: 14px;
            padding: 20px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='footer'>Developed by: Team 1</div>", unsafe_allow_html=True)