#!/usr/bin/env python3

import sys

#A ideia é testar o sys.argv e ver no que dá

nome = sys.argv[1]
corFavorita = sys.argv[2]
atividadeFavorita = sys.argv[3]
animalFavorito = sys.argv[4]

print("Olá, tudo bem? Meu nome é", sys.argv[1],". Minha cor favorita é", sys.argv[2],". O que eu mais gosto de fazer é", sys.argv[3]," e meu animal favorito é", sys.argv[4],".")
print("Olá, tudo bem? Meu nome é", sys.argv[1]+". Minha cor favorita é", sys.argv[2]+". O que eu mais gosto de fazer é", sys.argv[3]+" e meu animal favorito é", sys.argv[4]+".")
