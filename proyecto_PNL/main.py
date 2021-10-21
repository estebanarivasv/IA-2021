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


Tema elegido: #AppleEvent


"""
import nltk
import requests
import string
import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from wordcloud import WordCloud
from nltk.tokenize import TweetTokenizer
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import seaborn as sns

load_dotenv()

bearer_token = os.environ.get("BEARER_TOKEN")

url = "https://api.twitter.com/2/tweets/search/recent"
params = {
    'query': '#AppleEvent -is:retweet lang:en',
    'max_results': 100
}
headers = {
    "Authorization": f"Bearer {bearer_token}",
    "User-Agent": "v2FullArchiveSearchPython"
}


def get_data(url, params):
    response = requests.get(url, headers=headers, params=params)
    results = []
    i = 0

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
                'tweet.fields': 'created_at,entities',
                'user.fields': 'username',
                'next_token': token,
                'max_results': 100
            }
        i += 1
    return pd.concat(results)
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    print("Request metadata", dict(response.json())['meta'])

    df = pd.json_normalize(response.json()['data'])

    df.to_csv('tweets_apple_event.csv')


def tokenizacion(df):
    tt = TweetTokenizer()

    tokenized_text = df['text'].apply(tt.tokenize)
    df['tokenized_text'] = tokenized_text

    return df


def getToCsv():
    dd = pd.read_csv("tweets_apple_event.csv")
    return dd


def wordCloud(word_list):
    data = " ".join(map(str, word_list))
    wordcloud = WordCloud(max_words=100, background_color="white", collocations=False).generate(data)

    # Mostrar gráfico
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.rcParams['figure.figsize'] = [500, 500]
    plt.show()


def limpieza(dd):
    URL_REGEX = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s(" \
                r")<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’])) "
    MENTIONS_REGEX = r"(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9-_]+)"
    HASHTAG_REGEX = r"#"

    dd["text"].replace(URL_REGEX, '', regex=True, inplace=True)
    dd["text"].replace(MENTIONS_REGEX, '', regex=True, inplace=True)
    dd["text"].replace(HASHTAG_REGEX, '', regex=True, inplace=True)
    dd["text"].replace(r"[^A-Za-z0-9 | \n]+", ' ', regex=True, inplace=True)
    dd["text"].replace(r"\t", ' ', regex=True, inplace=True)
    dd["text"].replace('[{}]'.format(string.punctuation), ' ', regex=True, inplace=True)
    dd["text"].replace(r"\n", '', regex=True, inplace=True)

    return dd


def quitar_stopwords(dd):
    stopwords_list = stopwords.words('english')
    stopwords_list.append('https')
    stopwords_list.append('co')
    stopwords_list.append('t')
    stopwords_list.append('u')

    no_stopwords_data = []
    # Crear lista sin stopwords
    for x in dd['tokenized_text']:
        for word in x:
            if word.lower() not in stopwords_list:
                no_stopwords_data.append(word)

    return no_stopwords_data

def analisis_polaridad(serie):
    sentiment_analyzer = SentimentIntensityAnalyzer()
    df = serie.to_frame()
    df["negative"] = ""
    df["neutral"] = ""
    df["positive"] = ""
    df["result"] = ""
    df["compound"] = ""
    for index, row in df.iterrows():
        # Analizar cada review
        analisis = sentiment_analyzer.polarity_scores(row['text'])
        row["negative"] = analisis["neg"]
        row["neutral"] = analisis["neu"]
        row["positive"] = analisis["pos"]
        row["compound"] = analisis["compound"]
        # Evaluar que valores se considerarán positivo o negativo

        if analisis['compound'] >= 0.5 and analisis['compound'] <= 1:
            row["result"] = "Positive"

        elif analisis['compound'] <= -0.8:
            row["result"] = "Negative"

        else:
            row["result"] = "Neutral"

    return df

def etiquetado_POS_adj(tokenized_text):
    data_pos = nltk.pos_tag(tokenized_text)
    print(data_pos)
    adjetivos = []
    for k, v in data_pos:
        if k in ["AppleEvent", "notch", "laptop", "inch"]:
            continue
        if v in ["JJ", "JJR", "JJS"]:
            adjetivos.append(k)
    return adjetivos

if __name__ == '__main__':
    pd.set_option('display.max_columns', None)
    df = getToCsv()
    df = limpieza(df)

    # que es lo que esta pasando
    #df_situacion = df.copy(deep=False)
    #df_situacion["text"] = df_situacion["text"].str.lower()
    #df_situacion = tokenizacion(df_situacion)
    #wordCloud(quitar_stopwords(df_situacion))
    #input('enterrrr')
    #df_adjetivos = df.copy(deep=False)
    #df_adjetivos = tokenizacion(df_adjetivos)
    #adjetivos = quitar_stopwords(df_adjetivos)

    #wordCloud(etiquetado_POS_adj(adjetivos))

    df_analisis = analisis_polaridad(df['text'])
    sns.heatmap(df_analisis, cbar=False)


    print(df_analisis.info())
