#importar arquivos
lexicon = dict()

with open("./mus1.txt", "r", encoding="utf-8") as f:
    corpus1 = f.read()
    corpus1 = corpus1.lower()
    corpus1 = corpus1.replace("\n", " ").replace(".", " ").replace(",", " ").replace("!", " ").replace("?", " ")\
        .replace(":", " ").replace(";", " ").replace("-", " ").replace("(", " ").replace(")", " ").replace("  ", " ")
    corpus1 = corpus1.split(" ")
    set_corpus1 = set(corpus1)
    
    print(set_corpus1)
    print(len(set_corpus1))
    
with open("./mus2.txt", "r", encoding="utf-8") as f:
    corpus2 = f.read()
    corpus2 = corpus2.lower()
    corpus2 = corpus2.replace("\n", " ").replace(".", " ").replace(",", " ").replace("!", " ").replace("?", " ")\
        .replace(":", " ").replace(";", " ").replace("-", " ").replace("(", " ").replace(")", " ").replace("  ", " ")
    corpus2 = corpus2.split(" ")
    set_corpus2 = set(corpus2)
    print(set_corpus2)
    print(len(set_corpus2))

with open("./mus3.txt", "r", encoding="utf-8") as f:
    corpus3 = f.read()
    corpus3 = corpus3.lower()
    corpus3 = corpus3.replace("\n", " ").replace(".", " ").replace(",", " ").replace("!", " ").replace("?", " ")\
        .replace(":", " ").replace(";", " ").replace("-", " ").replace("(", " ").replace(")", " ").replace("  ", " ")
    corpus3 = corpus3.split(" ")
    set_corpus3 = set(corpus3)
    print(set_corpus3)
    print(len(set_corpus3))

with open("./lexico.txt", "+r", encoding="utf-8") as arquivo_lexico:
    linha = " "
    while linha != "":
        linha = arquivo_lexico.readline()   # =[,emot,-1,A
        #                                       0      1      2     3
        linha_split = linha.split(",")      # ['=[', 'emot', '-1', 'A']
        if len(linha_split) >= 3:
            chave = linha_split[0]      # '=['
            valor = int(linha_split[2]) # '-1' => -1
            lexicon[chave] = valor

soma_mus1 = 0
soma_mus2 = 0
soma_mus3 = 0
mus1_nao_lexico = []
mus2_nao_lexico = []
mus3_nao_lexico = []
mus1_no_lexico = []
mus2_no_lexico = []
mus3_no_lexico = []

for palavra in set_corpus1:
    if palavra not in lexicon:
        mus1_nao_lexico.append(palavra)
    else:
        valor = lexicon.get(palavra, 0)
        soma_mus1 += valor
        mus1_no_lexico.append(palavra)
for palavra in set_corpus2:
    if palavra not in lexicon:
        mus2_nao_lexico.append(palavra)
    else:
        valor = lexicon.get(palavra, 0)
        soma_mus2 += valor
        mus2_no_lexico.append(palavra)
for palavra in set_corpus3:
    if palavra not in lexicon:
        mus3_nao_lexico.append(palavra)
    else:
        valor = lexicon.get(palavra, 0)
        soma_mus3 += valor
        mus3_no_lexico.append(palavra)

print("=" * 50)
print("\nMus1 não no léxico:", mus1_nao_lexico)
print("\nMus2 não no léxico:", mus2_nao_lexico)
print("\nMus3 não no léxico:", mus3_nao_lexico)
print("=" * 50)
print("\nO texto Mus1 é: ", "POSITIVO" if soma_mus1 > 0 else "NEGATIVO" if soma_mus1 < 0 else "INDIFERENTE", "(", soma_mus1, ")")
print("\nO texto Mus2 é: ", "POSITIVO" if soma_mus2 > 0 else "NEGATIVO" if soma_mus2 < 0 else "INDIFERENTE", "(", soma_mus2, ")")
print("\nO texto Mus3 é: ", "POSITIVO" if soma_mus3 > 0 else "NEGATIVO" if soma_mus3 < 0 else "INDIFERENTE", "(", soma_mus3, ")")
print("=" * 50)
print("\nMus1 no lexico:", mus1_no_lexico)
print("\nMus2 no lexico:", mus2_no_lexico)
print("\nMus3 no lexico:", mus3_no_lexico)
print("=" * 50)

