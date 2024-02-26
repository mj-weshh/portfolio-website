from PIL import Image
import requests
import streamlit as st
import  streamlit_lottie

st.set_page_config(page_title="My Website", page_icon=":tada:", layout="wide")


def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Load Lottie animation
lottie_codding = load_lottie_url("https://lottie.host/008f92fb-e7d2-4044-9e7f-367cf332355a/lXNOoq4gtU.json")

# Load project images
me_img = Image.open("images/me.jpeg")
tic_img = Image.open("images/tic_tac_toe.png")
bmi_img = Image.open("images/bmi.png")
#coing_img = Image.open("images/coding.jpg")
password_img = Image.open("images/password.png")
rps_img = Image.open("images/rps.png")

# Introduction section
with st.container():
    st.subheader("Hi, I'm John Waweru Muhura :wave:")
    st.title("A Python Developer based in Nairobi, Kenya")
    st.write("A young fellow passionate to learn and explore, make a positive change for myself and for others")
    st.write("""
    [Github](https://github.com/mj-weshh)
    [Linked In](https://www.linkedin.com/in/john-muhura-165b83294/)
    """)

# Who I am section
with st.container():
    st.write("---")
    left_column, right_column = st.columns((2, 1))
    with left_column:
        st.header("Who I am")
        st.write("##")
        st.write(
            """
            ```
            I am a python developer
            I am a BSC Mathematics and Computer Science Student at Multimedia University of Kenya
            I am a software development student at power learn project
            I am a student at ALX undertaking AI Career Essentials (AICE)
            I am a member of the Muktimedia Science Student Association
            I am a craft lover
            I am a poet
            ```
            """)
        st.write("""
            ```
            I believe,
            'On reflection, postive change, by the minute, by the hour, for me, for others',
            is my mission!
            ```
""")
    with right_column:
        st.image(me_img)

# Skills section
with st.container():
    st.write("---")
    st.header("Skills")
    st.write("##")
    right, left = st.columns((2, 1))
    with right:
        st.subheader("Frontend development")
        st.write("Proficient in HTML, CSS, & JavaScript")
        st.subheader("Backend development")
        st.write("Experienced in Python")
        st.subheader("Version Control")
        st.write("Skilled in Git and GitHub")
        st.subheader("Soft Skills")
        st.write("Leadership, Teamwork, Time management, Swimming, and Ping Pong")
    with left:
        streamlit_lottie(lottie_codding, height=400, key="coding")

# Project sections
projects = [
    {
        'image': tic_img,
        'title': "Tic Tac Toe Game in Python",
        'description': "This is a simple implementation of the classic Tic Tac Toe game using Python and the Pygame library. You can play this game on your computer with two players taking turns.",
        'link': "https://github.com/mj-weshh/tic-tac-toe"
    },
    {
        'image': bmi_img,
        'title': "BMI Calculator",
        'description': "This Python script implements a Body Mass Index (BMI) calculator. The BMI is a measure of body fat based on weight and height. The script includes functions to calculate the BMI and classify it into different categories such as underweight, normal weight, overweight, or obese.",
        'link': "https://github.com/mj-weshh/OIBSIP/tree/main/bmi"
    },
    {
        'image': password_img,
        'title': "Random Password Generator",
        'description': "This Python script provides a simple command-line interface to generate random passwords based on user preferences. Users can specify the length of the password and choose whether to include letters, digits, and symbols.",
        'link': "https://github.com/mj-weshh/OIBSIP/tree/main/random_password_generator"
    },
    {
        'image': rps_img,
        'title': "Rock Paper Scissors Game",
        'description': "This Python script provides a simple command-line rock paper scissors game.",
        'link': "https://github.com/mj-weshh/rock-paper-scissors"
    },
]
with st.container():
        st.write("---")
        st.header("My Projects")
        st.write("##")
        for project in projects:
            
            image_column, text_column = st.columns((1, 2))
            with image_column:
                st.image(project['image'])
            with text_column:
                st.subheader(project['title'])
                st.write(project['description'])
                st.write(f"\n[Link to project]({project['link']})")
            st.write("---")
