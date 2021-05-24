import json

import nltk
from nltk.corpus import stopwords
arquivo_json = open('base_teste_json.json', 'r')
i = 0

for line in arquivo_json:
    i += 1
    dados_json = json.loads(line)
   # print(dados_json['text'])



#print(dados_json['user']['id'], dados_json['user']['screen_name'])



#stopword = ['a', 'agora', 'algum', "alguma", 'aquele', 'aquela', 'de', 'deu', 'do', 'e', 'estou', 'esta',
            #'ir', 'meu', 'muito', 'mesmo', 'no', 'nossa', 'o', 'outro', 'para', 'que', 'talvez', 'tem',
           # 'tendo', 'tenha', 'teve', 'tive', 'uma', 'um', 'umas', 'uns', 'vou']
stopwordsnltk = nltk.corpus.stopwords.words('portugues')
print(stopwordsnltk)
def removestopword(texto):
    frases = ()
    for (palavras, emocao) in texto:
        semstop = [p for p in palavras.split() if p not in stopwords]
        frases.append ((semstop, emocao))
    return frases

    prinf(removestoword[dados_json])

         #print(str(i) + " - tweets coletados")


#stemmer = nltk.stem.RSLPStemmer()

#stopwords = nltk.corpus.stopwords.words('portuguese')
#classificacoes = pd.read_csv('emails.csv', encoding = "utf8")

#textosPuros = classificacoes['email']
#marcas = classificacoes['classificacao']

#textosQuebrados = textosPuros.str.lower().str.split(' ')
#dicionario = set()

#for lista in textosQuebrados:
    #validas = [stemmer.stem(palavra) for palavra in lista if palavra not in stopwords and len(palavra) > 0]
    #dicionario.update(validas)