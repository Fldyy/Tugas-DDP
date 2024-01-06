import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from time import strftime

def hitung_skala_gempa():
    try:
        magnitude = float(entry_magnitude.get())
        if magnitude < 0:
            raise ValueError

        hasil = ""
        if magnitude < 4.0:
            hasil = "kecil"
        elif magnitude < 6.0:
            hasil = "sedang"
        elif magnitude < 8.0:
            hasil = "besar"
        else:
            hasil = "sangat besar"

        messagebox.showinfo("Hasil", "Gempa dengan skala " + str(magnitude) + " termasuk " + hasil + ".")

        if magnitude >= 7.0:
            messagebox.showwarning("Peringatan", "Gempa dengan skala " + str(magnitude) + " berpotensi berakibat tsunami!")
    except ValueError:
        messagebox.showerror("Error", "Masukkan magnitude yang valid!")

def tampilkan_seismograf():
    try:
        magnitude = float(entry_magnitude.get())
        if magnitude < 0:
            raise ValueError

        waktu = np.linspace(0, 10, 1000)
        amplitudo = magnitude * np.sin(waktu)

        plt.plot(waktu, amplitudo)
        plt.xlabel("Waktu (detik)")
        plt.ylabel("Amplitudo")
        plt.title("Seismograf")
        plt.show()
    except ValueError:
        messagebox.showerror("Error", "Masukkan magnitude yang valid!")
        

window = tk.Tk()
window.title("Aplikasi Skala Gempa")
window.geometry("300x200")

label_magnitude = tk.Label(window, text="Masukkan Magnitude:")
label_magnitude.pack(pady=20)

entry_magnitude = tk.Entry(window)
entry_magnitude.pack()

style = ttk.Style('vapor')
window.resizable(False,False)
  
button_hitung = tk.Button(window, text="Hitung", command=hitung_skala_gempa)
button_hitung.pack(pady=10)


button_seismograf = tk.Button(window, text="Tampilkan Seismograf", command=tampilkan_seismograf)
button_seismograf.pack()

window.mainloop()
