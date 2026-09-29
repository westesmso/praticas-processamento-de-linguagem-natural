import string

# etapa de coleta das letras
# 7 Minutes In Hell - Chrissy Costanza - https://www.letras.mus.br/chrissy-costanza/7-minutes-in-hell/#google_vignette
with open("mus1.txt", 'r', encoding='utf-8') as f:
    mus1 = f.read()

# O Carvalho e o Salgueiro - Karnival - https://www.letras.mus.br/karnival/o-carvalho-e-o-salgueiro/
with open("mus2.txt", 'r', encoding='utf-8') as f:
    mus2 = f.read()

# Diggy Diggy Hole - Wind Rose - https://www.letras.mus.br/wind-rose/diggy-diggy-hole/
with open("mus3.txt", 'r', encoding='utf-8') as f:
    mus3 = f.read()

# etapa de normalização e limpeza
mus1 = mus1.lower()
mus2 = mus2.lower()
mus3 = mus3.lower()

mus1 = mus1.translate(str.maketrans("", "", string.punctuation)).replace("\n", " ").replace("  ", " ")
mus2 = mus2.translate(str.maketrans("", "", string.punctuation)).replace("\n", " ").replace("  ", " ")
mus3 = mus3.translate(str.maketrans("", "", string.punctuation)).replace("\n", " ").replace("  ", " ")

# etapa de tokenização
mus1_tokens = mus1.split()
qtd_tokens_mus1 = len(mus1_tokens)
mus2_tokens = mus2.split()
qtd_tokens_mus2 = len(mus2_tokens)
mus3_tokens = mus3.split()
qtd_tokens_mus3 = len(mus3_tokens)

# criação dos vocabulários
mus1_vocab = set(mus1_tokens)
qtd_vocab_mus1 = len(mus1_vocab)
mus2_vocab = set(mus2_tokens)
qtd_vocab_mus2 = len(mus2_vocab)
mus3_vocab = set(mus3_tokens)
qtd_vocab_mus3 = len(mus3_vocab)

print(f"{'--'*10:<10} Tokens{'--'*10:<10}")
print("\nTokens da musica 1: \n", mus1_tokens)
print("\nQuantidade de tokens = ", qtd_tokens_mus1)
print(f"{'--'*25:<25}")

print("\nTokens da musica 2: \n", mus2_tokens)
print("\nQuantidade de tokens = ", qtd_tokens_mus2)
print(f"{'--'*25:<25}")

print("\nTokens da musica 3: \n", mus3_tokens)
print("\nQuantidade de tokens = ", qtd_tokens_mus3)
print(f"{'--'*25:<25}")

print(f"{'--'*10:<10} Vocabulário {'--'*10:<10}")
print("\nVocabulário da musica 1: ", mus1_vocab)
print("\nQuantidade de vocabulário = ", qtd_vocab_mus1)
print(f"{'--'*25:<25}")

print("\nVocabulário da musica 2: ", mus2_vocab)
print("\nQuantidade de vocabulário = ", qtd_vocab_mus2)
print(f"{'--'*25:<25}")

print("\nVocabulário da musica 3: ", mus3_vocab)
print("\nQuantidade de vocabulário = ", qtd_vocab_mus3)
print(f"{'--'*25:<25}")


# Riqueza lexical
riqueza_lexical_mus1 = qtd_vocab_mus1 / qtd_tokens_mus1 if qtd_tokens_mus1 > 0 else 0
riqueza_lexical_mus2 = qtd_vocab_mus2 / qtd_tokens_mus2 if qtd_tokens_mus2 > 0 else 0
riqueza_lexical_mus3 = qtd_vocab_mus3 / qtd_tokens_mus3 if qtd_tokens_mus3 > 0 else 0   

print(f"{'--'*10:<10} Riqueza Lexical {'--'*10:<10}")
print("\nRiqueza lexical da musica 1 = ", riqueza_lexical_mus1)
print(f"{'--'*25:<25}")
print("\nRiqueza lexical da musica 2 = ", riqueza_lexical_mus2)
print(f"{'--'*25:<25}")
print("\nRiqueza lexical da musica 3 = ", riqueza_lexical_mus3)
print(f"{'--'*25:<25}")