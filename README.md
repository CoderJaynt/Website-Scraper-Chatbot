# 🌐 Website QA Chatbot
<p align="center"> <img src="https://img.shields.io/badge/LLM-GROQ-purple?style=for-the-badge" /> <img src="https://img.shields.io/badge/Web%20Scraping-BeautifulSoup-green?style=for-the-badge" /> <img src="https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python" /> <img src="https://img.shields.io/badge/Mode-Console%20App-orange?style=for-the-badge" /> </p>
<br> <div align="center"> <h2>📚 Project Overview</h2> </div> <br> <div style=" background: linear-gradient(135deg,#141E30,#243B55); padding:25px; border-radius:18px; box-shadow: 0px 0px 20px rgba(36,59,85,0.5); color:white; line-height:1.8; "> <h3>🤖 What Does This Project Do?</h3>

### 📚 Project Overview
<div style=" background: linear-gradient(135deg,#141E30,#243B55); padding:25px; border-radius:18px; box-shadow: 0px 0px 20px rgba(36,59,85,0.5); color:white; line-height:1.8; ">
🤖 What Does This Project Do?

This project implements a console-based chatbot that can answer user queries
based on the content of a given website URL.

The system:

1. Scrapes website content using BeautifulSoup

2. Extracts and processes textual data

3. Sends structured context to GROQ LLM API

4. Generates intelligent, context-aware responses

</div>

### 💻 Platform Requirements
<div style=" background: linear-gradient(135deg,#42275a,#734b6d); padding:25px; border-radius:18px; box-shadow: 0px 0px 20px rgba(115,75,109,0.5); color:white; line-height:1.8; ">

* Operating System: Windows / macOS / Linux

* Python Version: Python 3.8 or higher

* Execution Mode: Local Machine (Terminal / Command Line)

</div>

### 📦 Dependencies
<div style=" background: linear-gradient(135deg,#1f4037,#99f2c8); padding:25px; border-radius:18px; box-shadow: 0px 0px 20px rgba(153,242,200,0.4); color:black; line-height:1.8; ">

All required libraries are listed in requirements.txt

Install using:
<pre> pip install -r requirements.txt </pre> </div>

### 🔑 API Key Setup
<div style=" background: linear-gradient(135deg,#000428,#004e92); padding:25px; border-radius:18px; box-shadow: 0px 0px 20px rgba(0,78,146,0.6); color:white; line-height:1.8; ">
Steps to Configure GROQ API Key

* Create an account on the GROQ Console

* Generate your API key

* Create a .env file in the project root directory

* Add the following line:

<pre> GROQ_API_KEY=your_api_key_here </pre>

 ### ⚠️ Never commit your API key to GitHub.

</div>

### ▶️ How to Run the Project
<div style=" background: linear-gradient(135deg,#134E5E,#71B280); padding:25px; border-radius:18px; box-shadow: 0px 0px 20px rgba(113,178,128,0.6); color:white; line-height:1.8; ">

Open your terminal and run:

<pre> python main.py </pre>

### The chatbot will start in the console and begin accepting queries.

</div>


#### ⭐ If you found this useful, consider giving the repo a star.
