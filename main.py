# Create a program that asks the user to type in an interval,
# and that finds the prime numbers in that interval.
# Criar um programa que peça para o usuário digitar um intervalo,
# e que encontre os números primos neste intervalo.

remainder_zero = 0
total_primes = 0

# Display initial text messages:
# Exibir mensagens de texto inicias:
print("Write the range in which to search for prime numbers.")
first_number = int(input("Enter the first number in the interval:\n"))
last_number = int(input("Enter the last number:\n"))
print("")
print("The prime numbers in this range are:")

# Criar um laço que vai usar cada um dos valores do intervalo digitado:
for i in range(first_number, (last_number+1)):

# Pegar cada valor do intervalo e dividir pelos números de 1 ao próprio valor.
# E caso o resto dessa divisão seja 0, adicionar 1 à variável resto_zero:
    for j in range(i+1):
        if j == 0:
            continue
        if (i % j == 0):
            remainder_zero += 1

# Caso o número de restos 0 seja igual a 2, trata-se de um número primo.
# Escrever esse número primo na tela.
# E adicionar 1 à variável total_primos.
    if remainder_zero == 2:
        print(i)
        total_primes += 1

# Zerar a variável resto_zero para que ela possa ser usada novamente pelo laço:
    remainder_zero = 0

# Escrever na tela total de primos encontrado:
print(f"In total, {total_primes} prime numbers were found.")