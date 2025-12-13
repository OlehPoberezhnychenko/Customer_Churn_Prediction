import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# CONFIGURATION
sns.set_theme(style="whitegrid")
DATA_PATH = 'data/WA_Fn-UseC_-Telco-Customer-Churn.csv'

# Ensure images folder exists
if not os.path.exists('images'):
    os.makedirs('images')

def load_data():
    if not os.path.exists(DATA_PATH):
        print(f"❌ ERROR: File not found at {DATA_PATH}")
        return None
    
    df = pd.read_csv(DATA_PATH)
    # Clean Data
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)
    df['Churn_Numeric'] = df['Churn'].map({'Yes': 1, 'No': 0})
    return df

# --- CHARTS 1, 2, 3 (Basic Analysis) ---
def plot_contract_risk(df):
    plt.figure(figsize=(10, 6))
    churn_rate = df.groupby('Contract')['Churn_Numeric'].mean() * 100
    sns.barplot(x=churn_rate.index, y=churn_rate.values, palette='Reds')
    plt.title('1. Churn Risk by Contract Type')
    plt.ylabel('Churn Rate (%)')
    plt.savefig('images/01_contract_risk.png', dpi=300)
    print("✅ Generated: 01_contract_risk.png")

def plot_tenure_dist(df):
    plt.figure(figsize=(10, 6))
    sns.kdeplot(data=df, x='tenure', hue='Churn', fill=True, palette=['green', 'red'], alpha=0.5)
    plt.title('2. Tenure Distribution')
    plt.savefig('images/02_tenure_distribution.png', dpi=300)
    print("✅ Generated: 02_tenure_distribution.png")

def plot_payment_method(df):
    plt.figure(figsize=(12, 6))
    churn_rate = df.groupby('PaymentMethod')['Churn_Numeric'].mean() * 100
    sns.barplot(x=churn_rate.index, y=churn_rate.values, palette='Blues_r')
    plt.title('3. Payment Method Churn')
    plt.xticks(rotation=15)
    plt.savefig('images/03_payment_method.png', dpi=300)
    print("✅ Generated: 03_payment_method.png")

# --- CHART 4 (Correlation) ---
def plot_correlation_matrix(df):
    # Select only numbers
    numeric_df = df.select_dtypes(include=[np.number])
    plt.figure(figsize=(10, 8))
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('4. Correlation Matrix')
    plt.tight_layout()
    plt.savefig('images/04_correlation_matrix.png', dpi=300)
    print("✅ Generated: 04_correlation_matrix.png")

# --- CHART 5 (Machine Learning) ---
def train_model(df):
    print("🤖 Training Model...")
    # Prepare Data
    X = df.drop(['customerID', 'Churn', 'Churn_Numeric'], axis=1)
    X = pd.get_dummies(X, drop_first=True)
    y = df['Churn_Numeric']
    
    # Split & Train
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    
    # Predict
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"✅ Accuracy: {accuracy:.1%}")
    
    # Plot Confusion Matrix
    plt.figure(figsize=(6, 5))
    sns.heatmap(confusion_matrix(y_test, predictions), annot=True, fmt='d', cmap='Blues')
    plt.title(f'5. Confusion Matrix (Acc: {accuracy:.1%})')
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    plt.savefig('images/05_confusion_matrix.png', dpi=300)
    print("✅ Generated: 05_confusion_matrix.png")

if __name__ == "__main__":
    df = load_data()
    if df is not None:
        plot_contract_risk(df)
        plot_tenure_dist(df)
        plot_payment_method(df)
        plot_correlation_matrix(df) # Generates Image 4
        train_model(df)             # Generates Image 5
