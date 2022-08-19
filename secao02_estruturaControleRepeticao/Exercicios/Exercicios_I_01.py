'''
Exercícios de Python -> Estrutura de Repetição

Exercício 1
---
Faça um script que mostre na tela uma contagem regressiva, de 10 até 0,
com uma pausa de 1 segundo entre cada exibição.
Dica: Para pausar você pode utilizar time.sleep().
'''
import time

for i in range(10,-1,-1):   # Contagem de 10 até 0
    print(i)
    time.sleep(1)           # Pausando 1 segundo
