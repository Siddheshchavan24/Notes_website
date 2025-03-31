import streamlit as st

# Load your HTML file
with open("index.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Render HTML in Streamlit
st.set_page_config(page_title="Notes Website", layout="wide")
st.components.v1.html(html_content, height=800, scrolling=True)
