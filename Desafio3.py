import os

palavra = (input("Digite uma palavra: ")).lower().strip()
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
palavraClone = palavra

for caractere in palavra:
    if (caractere != ' '):
        indexCaractere = (alfabeto.index(caractere) + 1)
        if (indexCaractere % 3 == 0):
            palavraClone = palavraClone.replace(caractere, str(indexCaractere))
            
print(palavraClone)

os.system("pause")
