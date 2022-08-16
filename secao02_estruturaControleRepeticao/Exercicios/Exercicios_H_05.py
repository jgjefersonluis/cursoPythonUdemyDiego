'''
Exercício 5
---
Crie um script que solicite o peso e a altura do usuário, depois calcule o IMC
dessa pessoa e mostre o seu status, de acordo com essa tabela:
Abaixo de 18.5 - Abaixo do ideal.
Entre 18.5 e 25 - Peso ideal.
De 25 até 30 - Sobrepeso.
De 30 até 40 - Obesidade.
Acima de 40 - Obesidade mórbida.
'''

peso = float(input('O seu peso é: '))
altura = float(input('A sua altura é: '))

imc = peso / (altura ** 2)
print('O seu IMC = {:.1f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
