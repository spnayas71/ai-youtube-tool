import streamlit as st
from gtts import gTTS
from PIL import Image, ImageDraw, ImageFont
import os

st.title("AI YouTube Video Tool")

# Input
topic = st.text_input("Enter your video topic (English only):")

if st.button("Generate Script"):
    if topic:
        script = f"""Title: {topic}\n\n[Intro]\nThis video is about {topic}, something you need to know.\n\n[Main]\nLet's break it down and show you the key facts, benefits, and real examples.\n\n[Outro]\nIf you enjoyed this video, like and subscribe for more just like it!"""
        st.text_area("Generated Script", script, height=200)

        # Save script
        with open("script.txt", "w") as f:
            f.write(script)

        # Generate voice
        tts = gTTS(script)
        tts.save("voice.mp3")
        st.audio("voice.mp3")

        # Generate thumbnail
        img = Image.new("RGB", (1280, 720), color=(0, 0, 0))
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 50)
        draw.text((50, 300), topic, font=font, fill=(255, 0, 0))
        img.save("thumbnail.png")
        st.image("thumbnail.png")

        # Export download links
        with open("script.txt", "rb") as f:
            st.download_button("Download Script", f, "script.txt")

        with open("voice.mp3", "rb") as f:
            st.download_button("Download Voice", f, "voice.mp3")

        with open("thumbnail.png", "rb") as f:
            st.download_button("Download Thumbnail", f, "thumbnail.png")
    else:
        st.warning("Please enter a topic first.")