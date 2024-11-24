import streamlit as st
from streamlit_navigation_bar import st_navbar
import base64
import pages as pg

st.set_page_config(
    initial_sidebar_state="collapsed",
    page_title="Hair Classification App",
    page_icon="images/icon.png",
)

pages = ["Home", "Detection", "About"]
styles = {
    "nav": {
        "background-color": "rgba(255, 255, 255, 0.5)",
        "max-width": "704px",
        "margin": "0 auto",
        "border-radius": "0.5rem",
        "box-shadow": "0 2px 4px 0 rgba(0, 0, 0, 0.1)",
        "backdrop-filter": "blur(16px)",
    },
    "div": {
        "max-width": "32rem",
    },
    "span": {
        "border-radius": "0.5rem",
        "color": "rgb(49, 51, 63)",
        "margin": "0 0.125rem",
        "padding": "0.4375rem 0.625rem",
    },
    "active": {
        "background-color": "rgba(255, 255, 255, 0.25)",
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",
    },
}

options = {
    "show_menu": False,
    "show_sidebar": False,
}

page = st_navbar(pages, styles=styles,options=options)

## get image background from images folder and convert to base64
with open("images/background.webp", "rb") as file:
    img = file.read()
    img_base64 = base64.b64encode(img).decode()

## set background image
# st.html(
#     f"""
#     <style>
#         .stApp {{
#             background-image: url('data:image/webp;base64,{img_base64}');
#             background-size: cover;
#         }}
#     </style>
#     """
# )

st.html(
    """
    <style>
        .stMarkdown {
            border-radius: 0.5rem;
            border: 1px solid rgba(255, 255, 255, 0.25);
            color: rgb(49, 51, 63);
            margin: 0.5rem 0;
            padding: 1rem;
            background-color: rgba(255, 255, 255);
        }
        h2{
            color: rgb(49, 51, 63);
        }
        h4{
            color: rgb(49, 51, 63);
        }
        img {
            border-radius: 2rem;
            margin: 0.5rem 0;
            padding: 0.5rem;
        }
        .stButton>button {
            background-color: #0ea5e9;
            border-radius: 0.5rem;
            color: white;
            margin: 0.5rem 0;
            padding: 0.5rem 1rem;
        }
        .stButton>button:hover {
            background-color: #075985;
            color: white;
            outline: none;
        }

    </style>
    """
)

functions = {
    "Home": pg.show_home,
    "Detection": pg.show_detection,
    "About": pg.show_about,
}
go_to = functions.get(page)
if go_to:
    go_to()