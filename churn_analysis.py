import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# CONFIGURATION
# Set the style for professional charts
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
    # Clean Data: Convert TotalCharges to numeric
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    # Encode Churn
    df['Churn_Numeric'] = df['Churn'].map({'Yes': 1, 'No': 0})
    return df

def plot_contract_risk(df):
    plt.figure(figsize=(10, 6))
    churn_rate = df.groupby('Contract')['Churn_Numeric'].mean() * 100
    ax = sns.barplot(x=churn_rate.index, y=churn_rate.values, palette='Reds')
    
    plt.title('1. Churn Risk by Contract Type', fontsize=14, fontweight='bold')
    plt.ylabel('Churn Rate (%)')
    plt.ylim(0, 50)
    
    # Add labels
    for i, v in enumerate(churn_rate.values):
        ax.text(i, v + 1, f"{v:.1f}%", ha='center', fontsize=12)
        
    plt.savefig('images/01_contract_risk.png', dpi=300)
    print("✅ Generated: images/01_contract_risk.png")

def plot_tenure_dist(df):
    plt.figure(figsize=(10, 6))
    # Plot distribution of churned vs retained
    sns.kdeplot(data=df, x='tenure', hue='Churn', fill=True, common_norm=False, palette=['green', 'red'], alpha=0.5)
    
    plt.title('2. Customer Tenure Distribution (When do they leave?)', fontsize=14, fontweight='bold')
    plt.xlabel('Months with Company')
    plt.xlim(0, 75)
    
    plt.savefig('images/02_tenure_distribution.png', dpi=300)
    print("✅ Generated: images/02_tenure_distribution.png")

def plot_payment_method(df):
    plt.figure(figsize=(12, 6))
    churn_rate = df.groupby('PaymentMethod')['Churn_Numeric'].mean() * 100
    # Sort for better visual
    churn_rate = churn_rate.sort_values(ascending=False)
    
    sns.barplot(x=churn_rate.index, y=churn_rate.values, palette='Blues_r')
    plt.title('3. Churn by Payment Method', fontsize=14, fontweight='bold')
    plt.ylabel('Churn Rate (%)')
    plt.xticks(rotation=15) # Rotate labels so they don't overlap
    
    plt.savefig('images/03_payment_method.png', dpi=300)
    print("✅ Generated: images/03_payment_method.png")

if __name__ == "__main__":
    print("--- Starting Analysis ---")
    df = load_data()
    if df is not None:
        plot_contract_risk(df)
        plot_tenure_dist(df)
        plot_payment_method(df)
        print("--- Analysis Complete ---")