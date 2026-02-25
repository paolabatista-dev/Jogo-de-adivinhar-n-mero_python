from random import randint
from time import sleep
r = randint(0,5)
print("\nVamos ver se você consegue acertar o número que eu estou pensando! \nVou te dar uma dica: é um número de 0 à 5.")
n = int(input("Digite seu número pensado aqui: "))

if 0 <= n <= 5:
    print("\nPROCESSANDO...")
    sleep(3)
    
    print(f"\nMeu número escolhido foi {r}!")

    if n == r:
        print("Parabéns, você acertou!")
    else:
        print("Que pena, você errou!")
else:
    print("Digite um número entre 0 e 5!")
