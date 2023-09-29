# 3D Surface Plotter
Script Python che mediante una minimale GUI prende in input una funzione in due variabili scritta usando NumPy (np) e che plotta mediante MatPlotLib un grafico tridimensionale della sua superficie con cui poter interagire.
## Perché usare 3D Surface Plotter?
Perché personalmente lo trovo molto più chiaro rispetto a programmi come Geogebra 3D per lo studio di superfici di funzioni in 2 variabili.
Ha diversi vantaggi rispetto a programmi come Geogebra 3D:
1. grafico colorato in base alla funzione rappresentata (con scala al lato)
2. possibilità di scaricare l'immagine con un click
3. possibilità di zoomare determinate sezioni dell'immagine
4. possibilità di studiare il grafico a 360 gradi
5. open source 😅

## Installazione:
1. Clonare questa repository / scaricare il file GUI-SurfacePlotter3D.py
2. Salvare il file nella cartella prescelta
3. Importare il file .py dentro a un IDE ed eseguirlo / spostarsi con il terminale nella cartella prescelta ed usare il seguente comando: `python3 GUI-SurfacePlotter3D.py` oppure `python GUI-SurfacePlotter3D.py` a seconda della versione utilizzata.

Per poter funzionare sono necessarie le seguenti librerie:
1. numpy
2. matplotlib.pyplot
3. tkinter

## Esempi:
<p align="center">
<img width="376" alt="Schermata 2023-09-29 alle 23 01 22" src="https://github.com/lorenzo-27/SurfacePlotter3D/assets/102320752/1686b0e4-f5ca-47a2-b9c4-f52795ef9d60" caption="">
<br>
GUI minimale per l'inserimento della funzione d'interesse.

<br>

<img width="375" alt="Schermata 2023-09-29 alle 23 04 51" src="https://github.com/lorenzo-27/SurfacePlotter3D/assets/102320752/0c62987b-5479-4b6c-8934-7ca7f19169a2">
<br>
Esempio di scrittura usando np della funzione f(x, y) = x^2 + y^2 .

<br>

<img width="642" alt="Schermata 2023-09-29 alle 23 05 01" src="https://github.com/lorenzo-27/SurfacePlotter3D/assets/102320752/8eca89ae-d75d-4d23-bb79-b83c86d618e5">
<br>
Grafico della funzione f(x, y) = x^2 + y^2 nella vista standard.

<br>

<img width="642" alt="Schermata 2023-09-29 alle 23 05 46" src="https://github.com/lorenzo-27/SurfacePlotter3D/assets/102320752/a5d08e81-653a-4e10-9852-ffe83860af77">
<br>
Dettaglio del grafico della funzione f(x, y) = x^2 + y^2 .
</p>

