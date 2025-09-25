import tkinter as tk
from tkinter import ttk, messagebox

class CronometroModern:
    def __init__(self, root):
        self.root = root
        self.root.title("Cronómetro Moderno")
        W, H = 420, 520
        self.root.geometry(f"{W}x{H}")
        self.root.resizable(False, False)

        # Canvas de fondo (degradado)
        self.canvas = tk.Canvas(self.root, width=W, height=H, highlightthickness=0)
        self.canvas.pack(fill='both', expand=True)

        # Gradient seguro: calcula colores dentro del rango 0-255
        for i in range(H):
            t = i / (H - 1)
            r = int(50 + t * 150)   # 50 -> ~200
            g = int(20 + t * 80)    # 20 -> ~100
            b = int(100 + t * 80)   # 100 -> ~180
            r = max(0, min(255, r))
            g = max(0, min(255, g))
            b = max(0, min(255, b))
            color = f"#{r:02x}{g:02x}{b:02x}"
            self.canvas.create_line(0, i, W, i, fill=color)

        # Variables del cronómetro
        self.tiempo = 0
        self.marchando = False
        self.after_id = None
        self.laps = []

        # Label del tiempo (visible sobre el canvas)
        self.time_var = tk.StringVar(value="00:00:00")
        label = tk.Label(self.root, textvariable=self.time_var,
                         font=("Consolas", 42, "bold"),
                         bg="#000000", fg="#00ffd1", bd=0)
        self.canvas.create_window(W//2, 80, window=label)

        # Frame para botones (se añade como window del canvas)
        frame = tk.Frame(self.root)
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 11, "bold"), padding=8)

        btn_start = ttk.Button(frame, text="▶ Iniciar", command=self.iniciar)
        btn_pause = ttk.Button(frame, text="⏸ Pausar", command=self.pausar)
        btn_reset = ttk.Button(frame, text="⟲ Reiniciar", command=self.reiniciar)
        btn_lap = ttk.Button(frame, text="🏁 Lap", command=self.lap)
        btn_save = ttk.Button(frame, text="💾 Guardar", command=self.guardar)

        btn_start.grid(row=0, column=0, padx=6, pady=6)
        btn_pause.grid(row=0, column=1, padx=6, pady=6)
        btn_reset.grid(row=0, column=2, padx=6, pady=6)
        btn_lap.grid(row=1, column=0, padx=6, pady=6)
        btn_save.grid(row=1, column=2, padx=6, pady=6)

        self.canvas.create_window(W//2, 200, window=frame)

        # Listbox para laps
        self.listbox = tk.Listbox(self.root, width=26, height=8, font=("Arial", 10))
        self.canvas.create_window(W//2, 370, window=self.listbox)

    def actualizar(self):
        if self.marchando:
            self.tiempo += 1
            h = self.tiempo // 3600
            m = (self.tiempo % 3600) // 60
            s = self.tiempo % 60
            self.time_var.set(f"{h:02}:{m:02}:{s:02}")
            self.after_id = self.root.after(1000, self.actualizar)
        else:
            self.after_id = None

    def iniciar(self):
        if not self.marchando:
            self.marchando = True
            if self.after_id is None:
                self.actualizar()

    def pausar(self):
        if self.marchando:
            self.marchando = False
            if self.after_id is not None:
                try:
                    self.root.after_cancel(self.after_id)
                except Exception:
                    pass
                self.after_id = None

    def reiniciar(self):
        self.pausar()
        self.tiempo = 0
        self.time_var.set("00:00:00")
        self.laps.clear()
        self.listbox.delete(0, tk.END)

    def lap(self):
        h = self.tiempo // 3600
        m = (self.tiempo % 3600) // 60
        s = self.tiempo % 60
        tstr = f"{h:02}:{m:02}:{s:02}"
        self.laps.append(tstr)
        self.listbox.insert(tk.END, tstr)

    def guardar(self):
        if not self.laps:
            messagebox.showinfo("Guardar", "No hay laps para guardar.")
            return
        try:
            with open("tiempos_cronometro.txt", "w", encoding="utf-8") as f:
                for t in self.laps:
                    f.write(t + "\n")
            messagebox.showinfo("Guardar", "Tiempos guardados en 'tiempos_cronometro.txt'.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CronometroModern(root)
    root.mainloop()
