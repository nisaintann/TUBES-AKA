import streamlit as st
import time
import matplotlib.pyplot as plt
from algorithms import count_primes_iterative, count_primes_recursive
import sys 
sys.setrecursionlimit(12000)

def measure_time(func, n_values):
    times = []
    for n in n_values:
        start = time.time()
        func(n)
        end = time.time()
        times.append(end - start)
    return times

# Streamlit App
st.title("Menghitung Jumlah Bilangan Prima dari 1 Hingga ke-N")

# Input N
n = st.number_input("Masukkan nilai N (integer positif):", min_value=1, step=1, value=10)

# Pilihan algoritma
algorithm = st.selectbox("Pilih algoritma:", ["Iteratif", "Rekursif"])

if st.button("Hitung Jumlah Bilangan Prima"):
    if algorithm == "Iteratif":
        st.write("Menghitung menggunakan algoritma **iteratif**...")
        result = count_primes_iterative(n)
    else:
        st.write("Menghitung menggunakan algoritma **rekursif**...")
        result = count_primes_recursive(n)
    st.success(f"Jumlah bilangan prima hingga {n}: {result}")

# Analisis Waktu Eksekusi
st.header("Analisis Waktu Eksekusi Algoritma Iteratif dan Rekursif")

n_values = st.multiselect(
    "Pilih ukuran masukan untuk analisis:",
    [10, 20, 50, 100, 200, 300, 500, 750, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
)

if st.button("Lakukan Analisis"):
    if n_values:
        iterative_times = measure_time(count_primes_iterative, n_values)
        recursive_times = measure_time(count_primes_recursive, n_values)

        # Plot hasil analisis
        st.write("**Hasil Analisis:**")
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(n_values, iterative_times, label="Iteratif", marker='o')
        ax.plot(n_values, recursive_times, label="Rekursif", marker='s')
            
        ax.set_xlabel("N")
        ax.set_ylabel("Waktu Eksekusi (seconds)")
        ax.set_title("Perbandingan Waktu Eksekusi: Iteratif vs Rekursif")
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)
    else:
        st.error("Silakan pilih setidaknya satu nilai untuk analisis.")
