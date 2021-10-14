"""

PROYECTO DE PROCESAMIENTO NATURAL DEL LENGUAJE

ENTREGA: 21/10/21

Consigna: Elegir un tema que queramos tratar (hashtag, palabra clave, que puede ser persona, evento, etc.)
y este debe estar optimizado para trabajar bien el tema.

Debemos extraer cualquier informacion util que sirva y con esos resultados generamos un reporte
con graficos y tablas

- Vamos a tener los resultados de los ultimos 7 dias.
- Cada grupo presenta el jueves que viene y muestra lo que el sistema genera
- Aplicar alguna de las tecnicas que hemos visto

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

