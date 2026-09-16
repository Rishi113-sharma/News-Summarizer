import streamlit as st
from base import get_news


st.title("📰 News Summarizer")

st.write("Search for the latest news and get a simple summary.")

query = st.text_input(
    "Enter news topic",
    placeholder="e.g. Latest ChatGPT news"
)


if st.button("Search & Summarize"):

    if query:

        with st.spinner("Searching and summarizing news..."):

            result = get_news(query)

        st.subheader("News Summary")
        st.write(result)

    else:
        st.warning("Please enter a news topic.")

