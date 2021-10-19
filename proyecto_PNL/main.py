"""

PROYECTO DE PROCESAMIENTO NATURAL DEL LENGUAJE

ENTREGA: 21/10/21

Consigna: Elegir un tema, persona, situación o evento. Este debe estar optimizado para trabajar bien el tema.

Crear un sistema que:

* Obtenga los Tweets asociados con dicho tema (Hashtag y/o Palabras claves)
* Aplique algunas de las técnicas de PNL (Tokenización, POS, Lematización, Derivación, Polarización)
* Obtener algunos de los siguientes datos 
    - ¿Quíenes están involucrados?
    - ¿De qué se trata?
    - ¿En qué lugares ocurre la acción?
    - ¿Qué opinion o sentimientos expresa la gente?
* Generar resultados (Gráficos, tablas)

- Vamos a tener los resultados de los ultimos 7 dias.
- Cada grupo presenta el jueves que viene y muestra lo que el sistema genera

Puntos a evaluar:
- Como se utilizaron las tecnicas
- Si la utilizaron bien
- Si la informacion de tweets buena/mala,
- Como elegimos armar los datos
- Presentacion oral.


Tema elegido: 


"""

import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Some text on Row 1')],
          [sg.Text('Enter something on Row 2'), sg.InputText()],
          [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()

