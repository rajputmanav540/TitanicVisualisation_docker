import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
titanic_df = sns.load_dataset('titanic')

# Streamlit App Title
st.title("Titanic Dataset Visualization")

# Sidebar Options
chart_type = st.sidebar.selectbox("Choose Chart Type", ["Survival Count", "Survival by Class", "Age Distribution", "Fare vs. Class"])

# Plot based on selection
if chart_type == "Survival Count":
    fig, ax = plt.subplots()
    sns.countplot(data=titanic_df, x='survived', palette='coolwarm', ax=ax)
    st.pyplot(fig)

elif chart_type == "Survival by Class":
    fig, ax = plt.subplots()
    sns.barplot(data=titanic_df, x='class', y='survived', hue='sex', palette='Set1', ax=ax)
    st.pyplot(fig)

elif chart_type == "Age Distribution":
    fig, ax = plt.subplots()
    sns.histplot(titanic_df['age'].dropna(), bins=30, kde=True, ax=ax)
    st.pyplot(fig)

elif chart_type == "Fare vs. Class":
    fig, ax = plt.subplots()
    sns.boxplot(data=titanic_df, x='class', y='fare', palette='muted', ax=ax)
    st.pyplot(fig)
