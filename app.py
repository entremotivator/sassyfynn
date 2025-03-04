import streamlit as st
import pandas as pd

# Set page title and layout
st.set_page_config(page_title="Sassy Fynn & Community", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Community", "Adventure Log"])

# Home Page
if page == "Home":
    st.title("Welcome to Sassy Fynn!")
    st.image("https://source.unsplash.com/featured/?adventure", use_column_width=True)
    st.write(
        "Sassy Fynn is a community for fearless explorers who love sharing their journeys, experiences, and tips. Join us and embark on exciting adventures together!"
    )
    st.subheader("Get Started:")
    st.write("- Share your latest adventure in the Adventure Log.")
    st.write("- Connect with like-minded adventurers in the Community.")

# Community Page
elif page == "Community":
    st.title("Sassy Community")
    st.write("Join the conversation and connect with fellow adventurers!")
    
    name = st.text_input("Enter your name:")
    message = st.text_area("Share something with the community:")
    if st.button("Post Message"):
        st.success(f"{name}, your message has been shared!")
    
    st.subheader("Recent Community Posts")
    community_posts = [
        {"name": "Alex", "message": "Just got back from hiking the Grand Canyon! What a view!"},
        {"name": "Jamie", "message": "Anyone here into skydiving? Looking for recommendations!"},
    ]
    for post in community_posts:
        st.write(f"**{post['name']}**: {post['message']}")

# Adventure Log Page
elif page == "Adventure Log":
    st.title("Adventure Log")
    st.write("Log your adventures and inspire others!")
    
    adventure = st.text_input("Adventure Title:")
    details = st.text_area("Describe your adventure:")
    image = st.file_uploader("Upload an image (optional)", type=["jpg", "png", "jpeg"])
    if st.button("Log Adventure"):
        st.success("Your adventure has been added!")
    
    st.subheader("Recent Adventures")
    adventure_logs = pd.DataFrame(
        {
            "Title": ["Climbing Mount Everest", "Diving in the Great Barrier Reef"],
            "Details": [
                "An incredible and life-changing experience. The altitude was tough but worth it!",
                "The marine life is stunning. Highly recommend for anyone who loves the ocean!",
            ],
        }
    )
    st.table(adventure_logs)
