import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk


# Funzione per calcolare e disegnare la superficie
def plot_surface():
    # Ottieni la funzione inserita dall'utente
    function_text = function_entry.get()

    # Crea una griglia di punti x e y
    x = np.linspace(-2, 2, 400)
    y = np.linspace(-2, 2, 400)
    X, Y = np.meshgrid(x, y)

    # Calcola il valore della funzione f(x, y) per ogni punto della griglia
    try:
        Z = eval(function_text)
    except Exception as e:
        result_label.config(text=f"Errore: {str(e)}")
        return

    # Crea il grafico tridimensionale
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Crea la superficie
    surface = ax.plot_surface(X, Y, Z, cmap='viridis')

    # Aggiungi una barra dei colori
    fig.colorbar(surface)

    # Etichette degli assi
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('f(x, y)')

    # Titolo del grafico
    plt.title('Superficie')

    # Mostra il grafico
    plt.show()


# Creazione della finestra principale
window = tk.Tk()
window.title("Grafico Superficie")

# Etichetta e box di testo per la funzione
function_label = ttk.Label(window, text="Inserisci la funzione:")
function_label.pack()
function_entry = ttk.Entry(window, width=40)
function_entry.pack()
function_label2 = ttk.Label(window, text="⚠️️ usa numpy e scrivi le variabili maiuscole", foreground="blue")
function_label2.pack()
# Pulsante per generare il grafico
plot_button = ttk.Button(window, text="Genera Grafico", command=plot_surface, padding=20)
plot_button.pack()

# Etichetta per i messaggi di errore
result_label = ttk.Label(window, text="")
result_label.pack()

# Avvia l'interfaccia grafica
window.mainloop()
