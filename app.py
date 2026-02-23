import streamlit as st
import requests
from bs4 import BeautifulSoup
from groq import Groq




def fetch_website_content(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching website: {e}")
        return None


def extract_text_from_html(html):
    soup = BeautifulSoup(html, "html.parser")

    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    text = soup.get_text(separator=" ")
    return text


def clean_text(text, max_length=4000):
    cleaned_text = " ".join(text.split())
    return cleaned_text[:max_length]


def build_prompt(context, question):
    prompt = f"""
You are a helpful chatbot.
Answer the user's question ONLY using the website content provided below.
If the answer is not found in the content, say:
"Information not available on the website."

Website Content:
{context}

User Question:
{question}
"""
    return prompt


def query_groq(api_key, prompt):
    client = Groq(api_key=api_key)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content




st.set_page_config(page_title="🌐 Website QA Chatbot", page_icon="🤖")

st.title("🌐 Website Question Answering Chatbot")
st.markdown("Ask questions based on any website content using GROQ LLM.")

# Step 1: API Key Input
st.subheader("🔐 Step 1: Enter GROQ API Key")
api_key = st.text_input("GROQ API Key", type="password")

# Step 2: Website URL
st.subheader("🌍 Step 2: Enter Website URL")
url = st.text_input("Website URL")

if st.button("Load Website"):
    if not api_key:
        st.warning("Please enter your GROQ API key first.")
    elif not url:
        st.warning("Please enter a website URL.")
    else:
        with st.spinner("Fetching and processing website content..."):
            html = fetch_website_content(url)

            if html:
                raw_text = extract_text_from_html(html)
                website_content = clean_text(raw_text)

                st.session_state.website_content = website_content
                st.success("Website loaded successfully! You can now ask questions.")



if "website_content" in st.session_state and api_key:

    st.subheader("❓ Step 3: Ask Questions")

    user_query = st.text_input("Your Question")

    if st.button("Ask"):
        if user_query.strip() == "":
            st.warning("Please enter a question.")
        else:
            with st.spinner("Generating answer..."):
                prompt = build_prompt(
                    st.session_state.website_content,
                    user_query
                )
                answer = query_groq(api_key, prompt)

                st.markdown("### 🤖 Bot Answer")
                st.write(answer)
