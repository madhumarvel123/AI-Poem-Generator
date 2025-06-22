import openai
import streamlit as st

load_dotenv() 
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="AI Poem/Story Generator", layout="centered")

st.title("📝 AI Poem Generator")
st.markdown("Enter a prompt and let GPT-3.5 create something magical ✨")

prompt = st.text_area("Enter your prompt here:", height=100)

if st.button("Generate"):
    if prompt.strip() == "":
        st.warning("Please enter a prompt before generating.")
    else:
        with st.spinner("Thinking..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "user", "content": prompt}
                    ]
                )
                output = response['choices'][0]['message']['content']
                st.subheader(" Generated Output")
                st.write(output)
            except Exception as e:
                st.error(f"Error: {str(e)}")

