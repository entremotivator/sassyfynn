import streamlit as st
import requests
from openai import OpenAI
import time

st.set_page_config(page_title="Sassy Fynn AI Image Generator", page_icon="🎨")

st.title("🎨 Sassy Fynn AI Image Generator")
st.markdown("Unleash your creativity with a dash of sass!")

# User input for API keys
st.sidebar.header("🔑 API Key Settings")
midjourney_api_key = st.sidebar.text_input("Midjourney API Key", type="password")
openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")

# User selects model
model_choice = st.radio("Choose your artistic muse:", ["Midjourney", "DALL·E", "Sassy Fynn Blend"])

# User input for prompt
prompt = st.text_area("Describe your masterpiece:", "A sassy robot painting a futuristic cityscape")

# Advanced options
st.sidebar.header("🛠️ Advanced Options")
image_size = st.sidebar.select_slider("Image Size", options=["256x256", "512x512", "1024x1024"], value="1024x1024")
style_intensity = st.sidebar.slider("Style Intensity", 0, 100, 50)

def generate_image():
    with st.spinner("Sassy Fynn is working her magic... 🎭"):
        if model_choice == "Midjourney":
            if not midjourney_api_key:
                st.error("Oops! Forgot your Midjourney API key? Sassy Fynn needs it to work her magic!")
                return
            
            response = requests.post(
                "https://api.midjourney.com/generate",
                json={"prompt": prompt, "style_intensity": style_intensity},
                headers={"Authorization": f"Bearer {midjourney_api_key}"},
            )
            if response.status_code == 200:
                image_url = response.json().get("image_url")
                st.image(image_url, caption="Midjourney's sassy creation", use_column_width=True)
            else:
                st.error(f"Midjourney threw a fit! Error: {response.text}")

        elif model_choice == "DALL·E":
            if not openai_api_key:
                st.error("DALL·E's feeling shy. Mind sharing your OpenAI API key?")
                return

            client = OpenAI(api_key=openai_api_key)
            try:
                response = client.images.generate(
                    model="dall-e-3",
                    prompt=prompt,
                    n=1,
                    size=image_size
                )
                image_url = response.data[0].url
                st.image(image_url, caption="DALL·E's artistic sass", use_column_width=True)
            except Exception as e:
                st.error(f"DALL·E's having a moment. Error: {str(e)}")

        elif model_choice == "Sassy Fynn Blend":
            st.info("Sassy Fynn is blending styles like a pro!")
            # Simulate a blended generation process
            for i in range(5):
                time.sleep(1)
                st.text(f"Blending styles... {(i+1)*20}%")
            st.image("https://picsum.photos/1024", caption="Sassy Fynn's unique blend", use_column_width=True)

# Generate button with sass
if st.button("Make Some Magic! ✨"):
    generate_image()

# Add some Sassy Fynn flair
st.sidebar.markdown("---")
st.sidebar.markdown("💁‍♀️ *Sassy Fynn says:* 'Darling, your creativity is showing!'")

# Easter egg
if prompt.lower() == "sassy fynn":
    st.balloons()
    st.markdown("You found me! I'm flattered, but let's create something more exciting than just little ol' me!")
