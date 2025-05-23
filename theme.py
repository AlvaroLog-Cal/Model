import streamlit as st

# Configure page
st.set_page_config(
    page_title="Predictor de Adhesión a Beneficios",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add custom CSS
st.markdown("""
<style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
        padding: 2rem;
        background-color: #f8f9fa;
    }
    
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 0.75rem 1.5rem;
        border-radius: 5px;
        font-weight: bold;
        transition: background-color 0.3s;
    }
    
    .stButton>button:hover {
        background-color: #45a049;
    }
    
    .stTable {
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    
    .stDataFrame {
        font-size: 16px;
    }
    
    .stSelectbox {
        margin-bottom: 1rem;
    }
    
    .stSlider {
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)
