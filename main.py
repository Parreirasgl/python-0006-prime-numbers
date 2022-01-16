# Create a program that asks the user to type in an interval,
# and that finds the prime numbers in that interval.
# Criar um programa que peça para o usuário digitar um intervalo,
# e que encontre os números primos neste intervalo.

remainder_zero = 0

# Display initial text messages:
# Exibir mensagens de texto inicias:
print("Write the range in which to search for prime numbers.")
print("")
first_number = input("Enter the first number in the interval:")
last_number = input("Enter the last number:")
print("")
print("The prime numbers in this range are:")

# Criar um laço que vai usar cada um dos valores do intervalo digitado:
for i in range(first_number, last_number+1):

# Pegar cada valor do intervalo e dividir pelos números de 1 ao próprio valor.
# E caso o resto dessa divisão seja 0, adicionar 1 à variável resto_zero:
    for j in range(i+1):
        if j == 0:
            continue
        if (i % j == 0):
            remainder_zero += 1
