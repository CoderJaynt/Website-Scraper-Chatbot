import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from groq import Groq


def load_environment():
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")

    return api_key


def fetch_website_content(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    
    except requests.exceptions.RequestException as e:
        print(f"Error Fetching website: {e}")
        return None
    

def extract_text_from_html(html):
    soup = BeautifulSoup(html, "html.parser")

    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    text = soup.get_text(separator=" ")
    
    return text


def clean_text(text, max_length = 4000):

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
    client = Groq(api_key = api_key)

    response = client.chat.completions.create(
        model = "llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature = 0.2
    )

    return response.choices[0].message.content


def main():
    print("Website ChatBot - Scaping test")

    url = input("Enter Website URL: ").strip()

    html = fetch_website_content(url)
    if not html:
        return
    
    raw_text = extract_text_from_html(html)
    website_content = clean_text(raw_text)

    print("\nWebsite loaded successfully!")
    print("Ask questions about the website (type 'exit' to quit)\n")

    while True:
        user_query = input("You: ").strip()

        if user_query.lower() == "exit":
            print("ChatBot exited")
            break

        api_key = load_environment()

        prompt = build_prompt(website_content, user_query)
        answer = query_groq(api_key, prompt)

        print(f"\nBot: {answer}\n")

if __name__ == "__main__":
    main()