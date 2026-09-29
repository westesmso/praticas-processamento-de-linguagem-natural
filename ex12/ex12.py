import os
os.makedirs("C:/temp", exist_ok=True)


# deixei um exemplo de texto para amostragem, porém o código funciona com qualquer arquivo de texto.
arquivo = input("Digite o diretório para o arquivo a ser copiado: ")

with open(arquivo, 'r', encoding='utf-8') as f:
    conteudo = f.read()

# with open("C:/temp/destino.txt", 'w', encoding='utf-8') as d:
#     conteudo = conteudo.replace("A", "4")
#     conteudo = conteudo.replace("B", "8")
#     conteudo = conteudo.replace("E", "3")
#     conteudo = conteudo.replace("G", "6")
#     conteudo = conteudo.replace("I", "1")
#     conteudo = conteudo.replace("q", "9")
#     conteudo = conteudo.replace("S", "5")
#     conteudo = conteudo.replace("T", "7")
#     conteudo = conteudo.replace("Z", "2")
#     d.write(conteudo)
    
## Esse é o conteúdo do exercício, porém, ele substitui apenas letras maiúsculas específicas por números.
# E para tornar mais interessante, vou adicionar também a normalização para tornar o texto em mínusculo e converter tudo. 
# Isso eu não fiz para a atividade visto que não é requisito, porém, achei legal pra ver resultados diferentes.

conteudo_lower = conteudo.lower()
paragrafos = conteudo_lower.split("\n")
with open("./destino.txt", 'w', encoding='utf-8') as d:
    for p in paragrafos:
        if p:
            p = p.replace("a", "4")
            p = p.replace("b", "8")
            p = p.replace("e", "3")
            p = p.replace("g", "6")
            p = p.replace("i", "1")
            p = p.replace("q", "9")
            p = p.replace("s", "5")
            p = p.replace("t", "7")
            p = p.replace("z", "2")
            p = p.replace("o", "0")
            p = p[0].upper() + p[1:]
            d.write(p + "\n\n")

# gostei do resultado.
