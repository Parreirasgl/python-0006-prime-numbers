# Create a program that asks the user to type in an interval,
# and that finds the prime numbers in that interval.
# Criar um programa que peça para o usuário digitar um intervalo,
# e que encontre os números primos neste intervalo.

remainder_zero = 0
total_primes = 0

# Display initial text messages:
# Exibir mensagens de texto inicias:
print("")
print("Write the range in which to search for prime numbers.")
first_number = int(input("Enter the first number in the interval:\n"))
last_number = int(input("Enter the last number:\n"))
print("")
print("The prime numbers in this interval are:")

# Create a loop that will use each of the values from the typed interval:
# Criar um laço que vai usar cada um dos valores do intervalo digitado:
for i in range(first_number, (last_number+1)):

# Take each value in the interval and divide it by the numbers from 1 to the value itself.
# And if the remainder of this division is 0, add 1 to the remainder_zero variable:
# Pegar cada valor do intervalo e dividir pelos números de 1 ao próprio valor.
# E caso o resto dessa divisão seja 0, adicionar 1 à variável remainder_zero:
    for j in range(i+1):
        if j == 0:
            continue
        if (i % j == 0):
            remainder_zero += 1

# If the value of reminder_zero is 2, i is a prime number.
# Write that prime number on the screen.
# And add 1 to the total_primes variable.
# Caso o valor do reminder_zero seja 2, i é um número primo.
# Escrever esse número primo na tela.
# E adicionar 1 à variável total_primes.
    if remainder_zero == 2:
        print(i, end=" ")
        total_primes += 1

# Reset the remainder_zero variable so that it can be used again by the loop:
# Zerar a variável remainder_zero para que ela possa ser usada novamente pelo laço:
    remainder_zero = 0

# Write on the screen total of primes found:
# Escrever na tela total de primos encontrado:
print("")
print(f"In total, {total_primes} prime numbers were found.")