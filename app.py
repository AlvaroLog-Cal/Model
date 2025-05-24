import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import plotly.graph_objects as go
import os

# Set page configuration
st.set_page_config(
    page_title="Predictor de Adhesión a Beneficios",
    page_icon="🎯",
    layout="wide"
)

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
            
            # Prepare DataFrame for all benefits
            df = pd.DataFrame({
                'Beneficio': [f"{benefit_options[b]} {b}" for b in predictions.keys()],
                'Tasa de Adhesión Predicha (%)': [round(v, 1) for v in predictions.values()]
            })

            # Define a function for conditional formatting
            def color_adhesion(val):
                if val >= 80:
                    color = 'background-color: #c6f6d5'  # light green
                elif val >= 60:
                    color = 'background-color: #fefcbf'  # light yellow
                else:
                    color = 'background-color: #fed7d7'  # light red
                return color


            
            # Create line graph data
            months = ['Mes 1', 'Mes 2', 'Mes 3', 'Mes 4', 'Mes 5', 'Mes 6']
            values = [np.random.uniform(30, 100) for _ in range(6)]
            
            # Create line graph
            fig = go.Figure()
            
            # Add line trace
            fig.add_trace(go.Scatter(
                x=months,
                y=values,
                mode='lines+markers',
                name='Tasa de Adhesión',
                line=dict(color='#2196F3', width=3),
                marker=dict(size=10)
            ))
            
            # Add trend line (linear regression)
            from sklearn.linear_model import LinearRegression
            model = LinearRegression()
            X = np.arange(len(months)).reshape(-1, 1)
            model.fit(X, values)
            trend_values = model.predict(X)
            
            fig.add_trace(go.Scatter(
                x=months,
                y=trend_values,
                mode='lines',
                name='Tendencia',
                line=dict(color='#4CAF50', dash='dash')
            ))
            
            # Update layout
            fig.update_layout(
                title=f'Evolución de la Tasa de Adhesión - {selected_benefit}',
                xaxis_title='Meses',
                yaxis_title='Tasa de Adhesión (%)',
                showlegend=True,
                legend=dict(
                    x=0.02,
                    y=0.98,
                    traceorder='normal',
                    bgcolor='rgba(255,255,255,0.8)',
                    bordercolor='rgba(0,0,0,0.2)',
                    borderwidth=1
                ),
                plot_bgcolor='rgba(245, 245, 245, 0.5)',
                paper_bgcolor='rgba(255,255,255,0.9)',
                margin=dict(l=50, r=50, t=80, b=50),
                height=400
            )
            
            # Add annotations
            fig.add_annotation(
                x=months[-1],
                y=values[-1],
                text=f'{values[-1]:.1f}%',
                showarrow=True,
                arrowhead=1,
                ax=-40,
                ay=-30,
                font=dict(color='#2196F3', size=12)
            )
            
            st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()

    # Add footer
    st.markdown("""
    <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f8f9fa;
            padding: 1rem;
            text-align: center;
            font-size: 0.8rem;
        }
    </style>
    <div class="footer">
        <p>Powered by AI & Data Science | Contacto: support@empresa.com | © 2025 Todos los derechos reservados</p>
    </div>
    """, unsafe_allow_html=True)
