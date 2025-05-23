import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor
import joblib

def preprocess_data(df):
    # Convert categorical variables to numerical
    le = LabelEncoder()
    df['INDUSTRIA/SECTOR'] = le.fit_transform(df['INDUSTRIA/SECTOR'])
    df['PERFIL MAYORITARIO (BLUE COLLAR & WHITE COLLAR)'] = df['PERFIL MAYORITARIO (BLUE COLLAR & WHITE COLLAR)'].map({
        'Blue Collar': 0, 'White Collar': 1
    })
    
    # Convert size ranges to midpoints
    size_mapping = {
        '100-250': 175,
        '250-500': 375,
        '500-1000': 750,
        '1000-5000': 2500
    }
    df['TAMAÑO POR EMPLEADOS'] = df['TAMAÑO POR EMPLEADOS'].map(size_mapping)
    
    # Drop the name column as it's not useful for prediction
    df = df.drop('NOMBRE', axis=1)
    
    return df

def train_models():
    # Load data
    df = pd.read_csv('Beneficios_Prediccion.CSV')
    
    # Preprocess data
    df = preprocess_data(df)
    
    # Define features and targets
    features = df.drop(['% DE ADHESIÓN BENEFICIO COMIDA',
                        '% DE ADHESIÓN BENEFICIO SALUD',
                        '% DE ADHESIÓN BENEFICIO GUARDERÍA',
                        '% DE ADHESIÓN BENEFICIO TRANSPORTE',
                        '% DE ADHESIÓN BENEFICIO FORMACIÓN'], axis=1)
    
    # Train separate models for each benefit
    benefit_models = {}
    for benefit in ['COMIDA', 'SALUD', 'GUARDERÍA', 'TRANSPORTE', 'FORMACIÓN']:
        target = f'% DE ADHESIÓN BENEFICIO {benefit}'
        X_train, X_test, y_train, y_test = train_test_split(
            features, df[target], test_size=0.2, random_state=42
        )
        
        # Train model
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        
        # Save model
        joblib.dump(model, f'model_{benefit.lower()}.pkl')
        benefit_models[benefit] = model
    
    return benefit_models

if __name__ == "__main__":
    benefit_models = train_models()
