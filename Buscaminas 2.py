import tkinter as tk
from tkinter import messagebox
import random
import time

class Buscaminas:
    def __init__(self, root, filas=8, columnas=8, minas=10):
        self.root = root
        self.root.title("Buscaminas Moderno")
        self.root.configure(bg="#1e1e2f")

        self.filas = filas
        self.columnas = columnas
        self.minas = minas
        self.timer = 0
        self.jugando = True

        # Panel superior
        top_frame = tk.Frame(root, bg="#252542")
        top_frame.pack(fill="x")

        self.label_minas = tk.Label(top_frame, text=f"💣 Minas: {minas}", font=("Arial", 12, "bold"), bg="#252542", fg="white")
        self.label_minas.pack(side="left", padx=10)

        self.label_tiempo = tk.Label(top_frame, text="⏱ 0s", font=("Arial", 12, "bold"), bg="#252542", fg="white")
        self.label_tiempo.pack(side="right", padx=10)

        self.boton_reset = tk.Button(top_frame, text="🔄 Reiniciar", command=self.reiniciar, bg="orange", fg="white")
        self.boton_reset.pack(side="bottom", pady=5)

        # Tablero
        self.frame_tablero = tk.Frame(root, bg="#1e1e2f")
        self.frame_tablero.pack()

        self.generar_tablero()
        self.colocar_minas()
        self.calcular_numeros()

        self.actualizar_timer()

    def generar_tablero(self):
        self.tablero = []
        self.botones = {}
        for i in range(self.filas):
            fila = []
            for j in range(self.columnas):
                boton = tk.Button(self.frame_tablero, width=3, height=1, font=("Arial", 12, "bold"),
                                  bg="#2c2c54", fg="white",
                                  command=lambda i=i, j=j: self.descubrir(i, j))
                boton.bind("<Button-3>", lambda e, i=i, j=j: self.marcar(i, j))
                boton.grid(row=i, column=j, padx=1, pady=1)
                self.botones[(i, j)] = boton
                fila.append(0)
            self.tablero.append(fila)

    def colocar_minas(self):
        minas_colocadas = 0
        while minas_colocadas < self.minas:
            i = random.randint(0, self.filas - 1)
            j = random.randint(0, self.columnas - 1)
            if self.tablero[i][j] != "M":
                self.tablero[i][j] = "M"
                minas_colocadas += 1

    def calcular_numeros(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.tablero[i][j] == "M":
                    continue
                minas_alrededor = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        ni, nj = i + x, j + y
                        if 0 <= ni < self.filas and 0 <= nj < self.columnas:
                            if self.tablero[ni][nj] == "M":
                                minas_alrededor += 1
                self.tablero[i][j] = minas_alrededor

    def descubrir(self, i, j):
        if not self.jugando:
            return
        boton = self.botones[(i, j)]
        if self.tablero[i][j] == "M":
            boton.config(text="💣", bg="red")
            messagebox.showerror("💥 Fin del juego", "¡Pisaste una mina!")
            self.jugando = False
        else:
            self.revelar_celda(i, j)
            if self.verificar_victoria():
                messagebox.showinfo("🎉 Victoria", "¡Ganaste el juego!")
                self.jugando = False

    def revelar_celda(self, i, j):
        if not (0 <= i < self.filas and 0 <= j < self.columnas):
            return
        boton = self.botones[(i, j)]
        if boton["state"] == "disabled":
            return
        valor = self.tablero[i][j]
        colores = ["#1e1e2f", "#00ffff", "#00ff00", "#ffcc00", "#ff6600", "#ff3300", "#cc00ff", "#ff0099", "#999999"]
        boton.config(text=str(valor) if valor > 0 else "", relief="sunken",
                     bg="#3c3c66", fg=colores[valor], state="disabled")
        if valor == 0:
            for x in range(-1, 2):
                for y in range(-1, 2):
                    self.revelar_celda(i + x, j + y)

    def marcar(self, i, j):
        boton = self.botones[(i, j)]
        if boton["text"] == "":
            boton.config(text="🚩", fg="red")
        elif boton["text"] == "🚩":
            boton.config(text="")

    def verificar_victoria(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.tablero[i][j] != "M" and self.botones[(i, j)]["state"] != "disabled":
                    return False
        return True

    def actualizar_timer(self):
        if self.jugando:
            self.timer += 1
            self.label_tiempo.config(text=f"⏱ {self.timer}s")
            self.root.after(1000, self.actualizar_timer)

    def reiniciar(self):
        self.frame_tablero.destroy()
        self.frame_tablero = tk.Frame(self.root, bg="#1e1e2f")
        self.frame_tablero.pack()
        self.timer = 0
        self.jugando = True
        self.label_tiempo.config(text="⏱ 0s")
        self.label_minas.config(text=f"💣 Minas: {self.minas}")
        self.generar_tablero()
        self.colocar_minas()
        self.calcular_numeros()

if __name__ == "__main__":
    root = tk.Tk()
    app = Buscaminas(root)
    root.mainloop()
