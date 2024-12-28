import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter
import pandas as pd

df = pd.read_csv("used_car_dataset.csv")

df = df.dropna()  
df = df[~df.duplicated()] 
df['kmDriven'] = (
    df['kmDriven']
    .str.replace(',', '')
        .str.replace('km', '')
        .str.strip()
        .apply(lambda x: int(float(x)))
)

df['AskPrice'] = (
    df['AskPrice']
    .str.replace(',', '')
    .str.replace('₹', '')
    .str.strip()
    .apply(lambda x: int(x) if x.isdigit() else None)
)

top_brands = df['Brand'].value_counts()

brand_price_avg = df.groupby('Brand')['AskPrice'].mean()

owner_counts = df['Owner'].value_counts()

st.title("Dashboard Mobil Bekas di Pasar India")

st.subheader("Top Merek Mobil Bekas")
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.barplot(x=top_brands.values, y=top_brands.index, palette='viridis', ax=ax1)
ax1.set_title('Top Merek Mobil Bekas di Pasar India', fontsize=16)
ax1.set_xlabel('Jumlah Mobil', fontsize=12)
ax1.set_ylabel('Merek', fontsize=12)
st.pyplot(fig1)

st.subheader("Hubungan Kilometer Tempuh dengan Harga Jual")
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=df, x='kmDriven', y='AskPrice', alpha=0.7, color='green', ax=ax2)
ax2.set_title('Hubungan Kilometer Tempuh dengan Harga Jual', fontsize=16)
ax2.set_xlabel('Kilometer Tempuh', fontsize=12)
ax2.set_ylabel('Harga Jual (₹)', fontsize=12)
ax2.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}'))
ax2.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}'))
st.pyplot(fig2)

st.subheader("Hubungan Usia Mobil dengan Harga Jual")
fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=df, x='Age', y='AskPrice', alpha=0.7, color='blue', ax=ax3)
ax3.set_title('Hubungan Usia Mobil dengan Harga Jual', fontsize=16)
ax3.set_xlabel('Usia Mobil (Tahun)', fontsize=12)
ax3.set_ylabel('Harga Jual (₹)', fontsize=12)
ax3.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}'))
ax3.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}'))
st.pyplot(fig3)

st.subheader("Rata-rata Harga Jual Berdasarkan Brand (Top 10)")
brand_price_avg_sorted = brand_price_avg.sort_values(ascending=False).head(10)
fig4, ax4 = plt.subplots(figsize=(12, 6))
sns.barplot(x=brand_price_avg_sorted.values, y=brand_price_avg_sorted.index, palette='magma', ax=ax4)
ax4.set_title('Rata-rata Harga Jual Berdasarkan Brand (Top 10)', fontsize=16)
ax4.set_xlabel('Rata-rata Harga Jual (₹)', fontsize=12)
ax4.set_ylabel('Brand', fontsize=12)
ax4.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}'))
st.pyplot(fig4)

st.subheader("Distribusi Kepemilikan Mobil Bekas")
owner_labels = owner_counts.index
owner_sizes = owner_counts.values
fig5, ax5 = plt.subplots(figsize=(8, 8))
ax5.pie(owner_sizes, labels=owner_labels, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'orange'])
ax5.set_title('Distribusi Kepemilikan Mobil Bekas', fontsize=16)
st.pyplot(fig5)
