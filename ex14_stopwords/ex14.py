import string
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# texto = """
# A inteligência artificial está cada vez mais presente no nosso dia a dia.
# A inteligência artificial pode ser utilizada para analisar textos,
# reconhecer imagens e auxiliar na tomada de decisões.
# A utilização da inteligência artificial em diferentes áreas está crescendo.
# A tecnologia pode ajudar empresas a analisar grandes quantidades de dados
# e pode auxiliar pessoas em diversas atividades.
# """

with open("D:\\programming\\Fatec\\PLN\\ex16_analise_sentimento_lexico\\mus1.txt", "r", encoding="utf-8") as f:
    texto = f.read()

texto = texto.lower()
texto_sem_pontuacoes = texto.translate(str.maketrans("","", string.punctuation))\
    .replace("\n", " ")\
    .replace("  ", " ")

texto_tokens = texto_sem_pontuacoes.split()

# print(texto_tokens)

stopwords = [
    "a", "o", "os", "as", "de", "do", "da",
    "e", "em", "no", "na", "para", "ser"
]

texto_sem_stopwords = [token for token in texto_tokens if token not in stopwords]
print(texto_sem_stopwords)

wordcloud = WordCloud(
    width=800,
    height=400,
    background_color="white",
    stopwords=stopwords,
    colormap="viridis",
    max_words=200,
    contour_color="black",
    contour_width=1
).generate(" ".join(texto_sem_stopwords))

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()