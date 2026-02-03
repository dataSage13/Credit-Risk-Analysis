import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# PAGE SETUP
# -------------------------
st.set_page_config(page_title="Credit Risk Dashboard", layout="wide")
st.title("📊 Credit Risk Dashboard")

# -------------------------
# LOAD DATA
# -------------------------
@st.cache_data
def load_data():
    application_df = pd.read_csv("data/application_record.csv")
    credit_df = pd.read_csv("data/credit_record.csv")

    credit_df['default'] = credit_df['STATUS'].apply(
        lambda x: 1 if x in ['1','2','3','4','5'] else 0
    )

    credit_summary = credit_df.groupby('ID').agg({
        'default': 'max',
        'MONTHS_BALANCE': 'min'
    }).reset_index()

    df = application_df.merge(credit_summary, on='ID', how='inner')
    return df

df = load_data()

# -------------------------
# DASHBOARD SECTIONS
# -------------------------
st.subheader("Default Distribution")
st.bar_chart(df['default'].value_counts())

st.subheader("Income vs Default")
fig, ax = plt.subplots()
df.boxplot(column='AMT_INCOME_TOTAL', by='default', ax=ax)
plt.suptitle("")
st.pyplot(fig)
