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

# import PySimpleGUI as sg

# sg.theme('DarkAmber')   # Add a touch of color
# # All the stuff inside your window.
# layout = [[sg.Text('Some text on Row 1')],
#           [sg.Text('Enter something on Row 2'), sg.InputText()],
#           [sg.Button('Ok'), sg.Button('Cancel')] ]

# # Create the Window
# window = sg.Window('Window Title', layout)
# # Event Loop to process "events" and get the "values" of the inputs
# while True:
#     event, values = window.read()
#     if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
#         break
#     print('You entered ', values[0])

# window.close()


import os
from dotenv import load_dotenv
from nltk.tokenize import TweetTokenizer
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import requests

load_dotenv()

bearer_token = os.environ.get("BEARER_TOKEN")

def getTweets():
    url = "https://api.twitter.com/2/tweets/search/recent"
    params = {
        'query': '#AppleEvent -is:retweet lang:en',
        'max_results':100
    }
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "User-Agent":"v2FullArchiveSearchPython"
    } 

   



def get_data(url,params):
    response = requests.get(url, headers=headers, params=params)
    results = []
    i =0

    while i <= 2000:
        response = requests.get(url, headers=headers, params=params)
        # Generar excepción si la respuesta no es exitosa
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)
        data = response.json()['data']
        meta_data = dict(response.json())['meta']
        results.append(pd.json_normalize(data))
        if 'next_token' not in meta_data:
            break
        else:
            token = meta_data['next_token']
            print("Token paginacion actual: ", token)
            params = {
                'query': '#AppleEvent -is:retweet lang:en',
                'tweet.fields':'created_at,entities',
                'user.fields':'username',
                'next_token':token,
                'max_results':100
            }
        i+=1
    return pd.concat(results)
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    print("Request metadata", dict(response.json())['meta'])




df = pd.json_normalize(response.json()['data'])

df.to_csv('tweets_apple_event.csv')  


def tokenizacion():
    tt = TweetTokenizer()

    tokenized_text = dd['text'].apply(tt.tokenize)
    dd['tokenized_text'] = tokenized_text


def getToCsv():
    dd = pd.read_csv("tweets_apple_event.csv")


def wordCloud():
    wordcloud = WordCloud(max_words=100, background_color="white").generate(dd['tokenized_text'].to_string())

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.rcParams['figure.figsize'] = [350, 350]
    plt.show()


def limpieza():
    URL_REGEX = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    MENTIONS_REGEX = r"(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9-_]+)"
    HASHTAG_REGEX = r"#"



    dd["text"].replace(URL_REGEX,'',regex=True, inplace = True)
    dd["text"].replace(MENTIONS_REGEX,'',regex=True, inplace = True)
    dd["text"].replace(HASHTAG_REGEX,'',regex=True, inplace = True)
    dd["text"].replace(r"[^A-Za-z0-9 | \n]+",' ',regex=True, inplace = True)
    dd["text"].replace(r"\t",' ',regex=True, inplace = True)
    dd["text"].replace('[{}]'.format(string.punctuation),' ',regex=True, inplace = True)
    dd["text"].replace(r"\n",'',regex=True, inplace = True)

    dd["text"] = dd["text"].str.lower()
    dd





































