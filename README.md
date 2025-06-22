# 📝 AI Poem Generator

## 📚 Project Overview

This is a simple app I built using Streamlit and OpenAI GPT-3.5 model.  
You type in any prompt — like "Write a poem about friendship in German" — and the app generates a creative response for you.

---

## 💡 What It Does

- Takes your prompt  
- Sends it to OpenAI GPT  
- Returns a poem or story based on what you asked  
- Lets you adjust creativity level and output length  
- You can download the result as a `.txt` file too

---

## ⚙️ How to Run It Locally

1. Clone this repo  
2. Install the required packages using `pip install -r requirements.txt`  
3. Create a `.env` file and paste your OpenAI API key like this:
   ```
   OPENAI_API_KEY=your-key-here
   ```
4. Run the app with:
   ```
   streamlit run app.py
   ```

---

## 🔒 A Quick Note

I did not include my real `.env` file here for safety.  
You can look at `.env.example` to see what format you need.

---

## 🎯 Why I Built This

I am learning Generative AI and wanted to build something fun and useful.  
This project helped me understand how to connect a front end with GPT and how to handle API keys securely.

Feel free to try it or improve it!
