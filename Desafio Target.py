print("-" * 20)
print('Desafio 01')

INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)



print("-" * 20)
print('Desafio 02')


def fibonacci(n):
    a, b = 0, 1
    sequencia_fibonacci = [a, b]   

    while a <= n:
        if a == n:
            return True, sequencia_fibonacci
        a, b = b, a + b
        sequencia_fibonacci.append(b)

    return False, sequencia_fibonacci


numero = int(input("Informe um número: "))

pertence, sequencia = fibonacci(numero)

print(f"\nSequência Fibonacci até {numero}: {sequencia}")

if pertence:
    print(f"\n{numero} pertence à sequência Fibonacci.")
else:
    print(f"\n{numero} não pertence à sequência Fibonacci.")



print("-" * 20)
print('Desafio 03')

    
print ('a) R= 9 A lógica é adicionar 2 ao número anterior')
print ('b) R= 128 A lógica é multiplicar 2 ao número anterior')
print ('c) R= 49 A lógica é  que cada numero é o quadrado de um número inteiro')
print ('d) R= 100 A lógica é que cada número é o quadrado de um numero par')
print ('e) R= 13 Sequencia Fibonnaci, onde cada numero é a soma dos dois anteriores')



print("-" * 20)
print('Desafio 04')

print('Primeiro, ligue um dos interruptores e espere um pouco até a lampada esquentar, depois desligue-o e ligue outro.') 
print('Quando você for até a sala das lâmpadas, a lâmpada que estiver acesa corresponde ao interruptor que você deixou ligado.')
print('A lâmpada que estiver apagada e quente corresponde ao interruptor que você ligou primeiro e depois desligou.')
print('A lâmpada que estiver apagada e fria corresponde ao interruptor que você nunca ligou. Assim, você consegue identificar qual interruptor controla cada lâmpada')



print("-" * 20)
print('Desafio 05')

texto = input("insira uma string: ")

texto_invertido = ''
for caractere in texto:
    texto_invertido = caractere + texto_invertido

print("A string invertida é:", texto_invertido)
