import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="ComicCraft AI", page_icon="🎨")
st.title("🎨 ComicCraft - AI Comic Story Creator")

api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")
prompt = st.text_area("Enter your story idea", "A girl who discovers a magical comic book")
genre = st.selectbox("Genre", ["Adventure", "Comedy", "Fantasy", "Sci-Fi"])
art_style = st.selectbox("Art Style", ["Comic", "Manga", "Cartoon", "Realistic"])

if st.button("Generate Comic"):
    if not api_key:
        st.error("Please enter Gemini API Key from aistudio.google.com")
    else:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-2.0-flash")
        story_prompt = f"Create a 5-panel comic story. Prompt: {prompt}, Genre: {genre}, Art Style: {art_style}. For each panel give scene description, caption and dialogue in JSON."
        
        with st.spinner("Gemini is creating your comic..."):
            response = model.generate_content(story_prompt)
            st.success("Comic Script Generated!")
            st.write(response.text)
            
            # For images - using Gemini image
            st.info("To generate images, use gemini-2.0-flash-exp-image-generation model")