import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import plotly.graph_objects as go

# Streamlit app
def main():
    # Banner with image
    try:
        header_image = Image.open('Gemini_Generated_Image_gwagxbgwagxbgwag.jpg')
        st.markdown("""
        <style>
            .header-image {
                width: 100%;
                height: auto;
                margin: 0;
                padding: 0;
                border: none;
                box-shadow: none;
            }
        </style>
        """, unsafe_allow_html=True)
        st.image(header_image, use_container_width=True)
    except FileNotFoundError:
        st.write("No se pudo cargar la imagen")
    
    # Banner content
    st.markdown("""
    <style>
        .prediction-box {
            background: white;
            padding: 1.5rem;
            border-radius: 10px;
            margin: 1rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            text-align: center;
        }
        
        .prediction-box h3 {
            color: #2196F3;
            margin-bottom: 0.5rem;
        }
        
        .prediction-value {
            font-size: 2rem;
            color: #2196F3;
        }
        
        .param-value {
            font-size: 1.2rem;
            font-weight: bold;
            color: #2196F3;
        }
        
        .param-label {
            color: #64b5f6;
            margin-bottom: 0.5rem;
        }
        
        .benefit-label {
            font-size: 1.2rem;
            color: #64b5f6;
        }
        
        .emoji {
            font-size: 1.5rem;
            margin-right: 0.5rem;
            vertical-align: middle;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Add a small spacer between image and content
    st.markdown("""
    <div style='height: 2rem;'></div>
    """, unsafe_allow_html=True)

    # Add subtitle above both columns
    st.markdown("""
    <div style='text-align: center; margin-bottom: 2rem;'>
        <h3 style='color: #2196F3;'>Introduzca los datos de su empresa</h3>
    </div>
    """, unsafe_allow_html=True)

    # Create two columns for parameters and predictions
    col1, col2 = st.columns([1, 1])
    
    # Parameters in first column
    with col1:
        industry = st.selectbox(
            'Industria/Sector',
            ['Tecnología', 'Salud', 'Educación', 'Finanzas', 'Manufactura', 'Retail', 'Otro']
        )
        
        size = st.slider(
            'Tamaño de la Empresa (empleados)',
            100, 5000, 500
        )
        
        profile = st.selectbox(
            'Perfil Mayoritario',
            ['Blue Collar', 'White Collar']
        )
        
        avg_age = st.number_input(
            'Edad Media de la Empresa (años)',
            min_value=1,
            max_value=100,
            value=10,
            step=1
        )
        

    
    # Predictions in second column
    with col2:
        # Benefit selection with emojis
        benefit_options = {
            'COMIDA': '🍽️',
            'SALUD': '🏥',
            'GUARDERÍA': '👶',
            'TRANSPORTE': '🚗',
            'FORMACIÓN': '🎓'
        }
        
        selected_benefit = st.selectbox(
            'Selecciona el beneficio a predecir',
            list(benefit_options.keys()),
            format_func=lambda x: f"{benefit_options[x]} {x}"
        )
        
        if st.button('Predecir Adhesión'):
            # Generate random predictions
            predictions = {
                'COMIDA': np.random.uniform(60, 90),
                'SALUD': np.random.uniform(70, 95),
                'GUARDERÍA': np.random.uniform(40, 80),
                'TRANSPORTE': np.random.uniform(50, 85),
                'FORMACIÓN': np.random.uniform(65, 90)
            }
            
            # Display selected benefit prediction with a gauge chart
            if selected_benefit in predictions:
                prediction = predictions[selected_benefit]
                st.markdown(f"<div class='prediction-box'>"
                           f"<h3>Tasa de Adhesión Predicha</h3>"
                           f"<div class='prediction-value'>{prediction:.1f}%</div>"
                           f"<p class='benefit-label'>{benefit_options[selected_benefit]} {selected_benefit}</p>"
                           f"</div>", unsafe_allow_html=True)
            
            value = predictions[selected_benefit]
            
            fig = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = value,
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': f"Tasa de Adhesión {selected_benefit}"},
                gauge = {
                    'axis': {'range': [None, 100]},
                    'bar': {'color': "#2196F3"},
                    'steps' : [
                        {'range': [0, 30], 'color': "#FF4444"},
                        {'range': [30, 70], 'color': "#FFBB33"},
                        {'range': [70, 100], 'color': "#4CAF50"}
                    ],
                    'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 70}
                }
            ))
            
            st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
