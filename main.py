import streamlit as st
import time
import matplotlib.pyplot as plt
from algorithms import count_primes_iterative, count_primes_recursive
import sys 
sys.setrecursionlimit(30000)

# Streamlit App
st.title("Menghitung Jumlah Bilangan Prima dari 1 Hingga ke-N")

# Input N
n = st.number_input("Masukkan nilai N (integer positif):", min_value=1, step=1, value=10)

# Pilihan algoritma
algorithm = st.selectbox("Pilih algoritma:", ["Iteratif", "Rekursif"])

if st.button("Hitung Jumlah Bilangan Prima"):
    if algorithm == "Iteratif":
        st.write("Menghitung menggunakan algoritma **iteratif**...")
        start_time = time.time()  # Waktu mulai
        result = count_primes_iterative(n)
        end_time = time.time()  # Waktu selesai
    else:
        st.write("Menghitung menggunakan algoritma **rekursif**...")
        start_time = time.time()  # Waktu mulai
        result = count_primes_recursive(n)
        end_time = time.time()  # Waktu selesai
    
    elapsed_time = end_time - start_time
    st.success(f"Jumlah bilangan prima dari 1 hingga {n}: {result}")
    st.info(f"Waktu eksekusi: {elapsed_time:.6f} detik")

