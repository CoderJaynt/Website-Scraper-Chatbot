# PROJECT OVERVIEW
This project implements a console-based chatbot that can answer user queries based on the content of a given website URL.

The chatbot scrapes the website using Beautiful Soup, processes the extracted text, and uses the GROQ LLM API to generate context-aware responses.


# PLATFORM REQUIREMENTS
This project runs on:

1. Operating System: Windows / macOS / Linux

2. Python Version: Python 3.8 or higher

3. Execution Mode: Local machine (Command Line / Terminal)


# DEPENDENCIES
All required dependencies are listed in requirements.txt

Install them using:

************************************
pip install -r requirements.txt
************************************


# API KEY REQUIREMENT
Steps to Set Up API Key:

1. Create an account on the GROQ Console

2. Generate an API key

3. Create a .env file in the project root directory

4. Add the following line:

**********************************
5. GROQ_API_KEY=your_api_key_here
**********************************


# HOW TO RUN THE PROJECT
Run the application :

write this command in your terminal:

*****************
python main.py

*****************
