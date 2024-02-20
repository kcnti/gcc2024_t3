import streamlit as st
import requests
from instaloader import Instaloader, Profile
from facebook_scraper import get_profile

st.title("Scam Detector")

def save_image(url, file_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, "wb") as file:
            file.write(response.content)
        print("Successed")
    else:
        print("failed")

def collect_fb_profile(username):
    result = get_profile(username)
    return result

def collect_insta_profile(username):
    L = Instaloader()
    profile = Profile.from_username(L.context, username)
    UserName = profile.full_name 
    posts = profile.mediacount
    Follower = profile.followers
    Follow = profile.followees
    return profile

username = st.text_input("username")

if st.button("Run"):

    insta_profile = collect_insta_profile(username)
    st.write("Name:",insta_profile.full_name)
    st.write("Post:",insta_profile.mediacount)
    st.write("Followers:",insta_profile.followers)
    st.write("Followees:",insta_profile.followees)

    fb_profile = collect_fb_profile(username)
    st.write(fb_profile)
    
    save_image(fb_profile["profile_picture"], "fb_icon.png")
    save_image(fb_profile["cover_photo"], "fb_cover.png")

    st.write("Name:",fb_profile["Name"])
    st.image("fb_icon.png")
    st.image("fb_cover.png")
