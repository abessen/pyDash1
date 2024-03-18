from PIL import Image
import streamlit as st
import subprocess
import threading
import os
import time
import sys  # Add this line for importing sys

# Set Page Configuration
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)  

st.markdown(
    """
    <style>
    .reportview-container .viewer .stApp .footer {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("""
    <style>
    body {
        background-color: #f0f0f0;
    }
    </style>
    """, unsafe_allow_html=True)

# Local path to the image
    image_path = "ColLSToday.jpg"

    # Load the image using the cached function
    image = load_image(image_path)

    # Display the image to automatically resize with the column width
    st.image(image, use_column_width=True)

    # Wait for 60 seconds before the next iteration
    time.sleep(60)  
    rerun()



if __name__ == '__main__':
    main()


