import streamlit as st
import sqlite3
import string
import random

conn = sqlite3.connect('database.db', check_same_thread=False)
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS urls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    original_url TEXT NOT NULL,
    short_url TEXT NOT NULL UNIQUE
)
''')
conn.commit()

def generate_short_url():
    characters = string.ascii_letters + string.digits
    while True:
        short_url = ''.join(random.choices(characters, k=6))
        c.execute('SELECT * FROM urls WHERE short_url = ?', (short_url,))
        if not c.fetchone():
            return short_url

def save_url(original_url, short_url):
    c.execute('INSERT INTO urls (original_url, short_url) VALUES (?, ?)', (original_url, short_url))
    conn.commit()

def get_original_url(short_url):
    c.execute('SELECT original_url FROM urls WHERE short_url = ?', (short_url,))
    result = c.fetchone()
    if result:
        return result[0]
    return None

st.title("Shrnk.ly - URL Shortener")

original_url = st.text_input("Enter the URL to shorten:")

if st.button("Generate Short URL"):
    if original_url:
        short_url = generate_short_url()
        save_url(original_url, short_url)
        st.success(f"Short URL: https://shrnk.ly/{short_url}")
    else:
        st.error("Please enter a valid URL")

st.markdown("---")
st.subheader("Retrieve Original URL from Short Code")
short_code = st.text_input("Enter the short code:")

if st.button("Get Original URL"):
    if short_code:
        url = get_original_url(short_code)
        if url:
            st.info(f"Original URL: {url}")
        else:
            st.error("Short URL not found")
    else:
        st.error("Please enter a short code")
