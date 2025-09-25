import tkinter as tk
from tkinter import messagebox
import math

# ==== FUNCIONES ====
def calcular(operacion, event=None):
    a_str = entry_a.get()
    b_str = entry_b.get()
    try:
        a = float(a_str)
        b = float(b_str)
    except ValueError:
        messagebox.showerror("Entrada inválida", "Por favor ingresa dos números válidos.")
        return

    if operacion == "suma":
        resultado = a + b
        resultado_var.set(f"Suma: {resultado:g}")
    elif operacion == "resta":
        resultado = a - b
        resultado_var.set(f"Resta: {resultado:g}")
    elif operacion == "multiplicacion":
        resultado = a * b
        resultado_var.set(f"Multiplicación: {resultado:g}")
    elif operacion == "division":
        if b == 0:
            messagebox.showerror("Error", "No se puede dividir entre cero.")
            return
        resultado = a / b
        resultado_var.set(f"División: {resultado:g}")
    elif operacion == "raiz_cuadrada":
        try:
            raiz_a = math.sqrt(a)
            raiz_b = math.sqrt(b)
            resultado_var.set(f"√A={raiz_a:g}, √B={raiz_b:g}")
        except ValueError:
            messagebox.showerror("Error", "No se pueden calcular raíces de números negativos.")
    elif operacion == "raiz_cubica":
        raiz_a = a ** (1/3) if a >= 0 else -((-a) ** (1/3))
        raiz_b = b ** (1/3) if b >= 0 else -((-b) ** (1/3))
        resultado_var.set(f"∛A={raiz_a:g}, ∛B={raiz_b:g}")
    elif operacion == "potencia":
        try:
            pot_ab = a ** b
            pot_ba = b ** a
            resultado_var.set(f"A^B={pot_ab:g}, B^A={pot_ba:g}")
        except OverflowError:
            messagebox.showerror("Error", "El resultado es demasiado grande.")
    elif operacion == "seno":
        resultado = math.sin(a)
        resultado_var.set(f"sen(A)={resultado:g}")
    elif operacion == "coseno":
        resultado = math.cos(a)
        resultado_var.set(f"cos(A)={resultado:g}")
    elif operacion == "tangente":
        try:
            resultado = math.tan(a)
            resultado_var.set(f"tan(A)={resultado:g}")
        except Exception:
            messagebox.showerror("Error", "No se puede calcular la tangente en este valor.")

def limpiar():
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    resultado_var.set("Resultado: ")

# ==== INTERFAZ ====
root = tk.Tk()
root.title("Calculadora Avanzada")
root.geometry("380x520")
root.config(bg="#1E3A8A")  # Azul fuerte
root.resizable(False, False)

# Estilos
fuente = ("Segoe UI", 11, "bold")
btn_azul = {"bg": "#1D4ED8", "fg": "white", "activebackground": "#2563EB", "activeforeground": "white"}
btn_amarillo = {"bg": "#FACC15", "fg": "black", "activebackground": "#FCD34D", "activeforeground": "black"}

# Entradas
frame_top = tk.Frame(root, bg="#1E3A8A")
frame_top.pack(pady=15)

tk.Label(frame_top, text="Número A:", font=fuente, fg="white", bg="#1E3A8A").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_a = tk.Entry(frame_top, font=fuente, justify="center", width=12)
entry_a.grid(row=0, column=1, padx=5, pady=5)
entry_a.focus()

tk.Label(frame_top, text="Número B:", font=fuente, fg="white", bg="#1E3A8A").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_b = tk.Entry(frame_top, font=fuente, justify="center", width=12)
entry_b.grid(row=1, column=1, padx=5, pady=5)

# Botones
frame_btn = tk.Frame(root, bg="#1E3A8A")
frame_btn.pack(pady=10)

# Operaciones básicas
tk.Button(frame_btn, text="Sumar", width=12, height=2, command=lambda: calcular("suma"), **btn_azul).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame_btn, text="Restar", width=12, height=2, command=lambda: calcular("resta"), **btn_azul).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame_btn, text="Multiplicar", width=12, height=2, command=lambda: calcular("multiplicacion"), **btn_azul).grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame_btn, text="Dividir", width=12, height=2, command=lambda: calcular("division"), **btn_azul).grid(row=1, column=1, padx=5, pady=5)

# Raíces y potencias
tk.Button(frame_btn, text="Raíz Cuadrada", width=12, height=2, command=lambda: calcular("raiz_cuadrada"), **btn_amarillo).grid(row=2, column=0, padx=5, pady=5)
tk.Button(frame_btn, text="Raíz Cúbica", width=12, height=2, command=lambda: calcular("raiz_cubica"), **btn_amarillo).grid(row=2, column=1, padx=5, pady=5)
tk.Button(frame_btn, text="Potencias", width=26, height=2, command=lambda: calcular("potencia"), **btn_amarillo).grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Funciones trigonométricas
tk.Button(frame_btn, text="Seno (A)", width=12, height=2, command=lambda: calcular("seno"), **btn_azul).grid(row=4, column=0, padx=5, pady=5)
tk.Button(frame_btn, text="Coseno (A)", width=12, height=2, command=lambda: calcular("coseno"), **btn_azul).grid(row=4, column=1, padx=5, pady=5)
tk.Button(frame_btn, text="Tangente (A)", width=26, height=2, command=lambda: calcular("tangente"), **btn_azul).grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Botón limpiar (amarillo)
tk.Button(root, text="Limpiar", width=26, height=2, command=limpiar, **btn_amarillo).pack(pady=5)

# Resultado
resultado_var = tk.StringVar(value="Resultado: ")
tk.Label(root, textvariable=resultado_var, font=("Segoe UI", 13, "bold"),
         fg="#FACC15", bg="#1E3A8A").pack(pady=15)

# Enter ejecuta suma
root.bind("<Return>", lambda event: calcular("suma"))

root.mainloop()
