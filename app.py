# Streamlit Web App RAB Gedung
import streamlit as st
import pandas as pd

st.title("RAB Gedung Kalkulator")

# Input proyek
nama_proyek = st.text_input("Nama Proyek", "Gedung A")
panjang = st.number_input("Panjang (m)", 10.0)
lebar = st.number_input("Lebar (m)", 8.0)
tinggi = st.number_input("Tinggi (m)", 3.0)

# Data bahan & upah
data_satuan = {
    'Bahan': ['Batu','Pasir','Bata','Semen','Upah Tukang'],
    'Satuan': ['m3','m3','buah','sak','hari'],
    'Harga Satuan': [280000, 400000, 4000, 200000, 200000]
}
df_satuan = pd.DataFrame(data_satuan)

# Input volume
volume_batu = st.number_input("Volume Pondasi Batu (m3)", 10.0)
volume_pasir = st.number_input("Volume Pasir Pondasi (m3)", 5.0)
volume_bata = st.number_input("Jumlah Bata (buah)", 1000)
volume_semen = st.number_input("Jumlah Sak Semen", 50)
volume_upah = st.number_input("Jumlah Hari Upah Tukang", 20)

# Hitung biaya
biaya_bahan = [
    volume_batu*280000,
    volume_pasir*400000,
    volume_bata*4000,
    volume_semen*200000,
    0
]
biaya_upah = [
    biaya_bahan[0]*0.4,
    biaya_bahan[1]*0.4,
    biaya_bahan[2]*0.4,
    biaya_bahan[3]*0.4,
    volume_upah*200000
]
total = [b+h for b,h in zip(biaya_bahan,biaya_upah)]

# Tampilkan tabel
df_rab = pd.DataFrame({
    'Uraian Pekerjaan': ['Pondasi Batu','Pasir Pondasi','Dinding Bata','Semen','Upah Tukang'],
    'Volume': [volume_batu, volume_pasir, volume_bata, volume_semen, volume_upah],
    'Satuan': ['m3','m3','buah','sak','hari'],
    'Biaya Bahan': biaya_bahan,
    'Biaya Upah': biaya_upah,
    'Total Biaya': total
})

st.subheader("RAB Gedung")
st.dataframe(df_rab)

st.write("**Total Keseluruhan:** Rp", sum(total))

