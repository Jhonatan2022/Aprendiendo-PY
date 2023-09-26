# Fizz Fuzz
# Imprimir los números del 1 al 100
for num in range(1, 101):
    # Si el número es divisible entre 3 y 5, imprimir FizzBuzz
    if num % 15 == 0:
        # Si el número es divisible entre 3, imprimir Fizz
        print(num, "  FizzBuzz")

        # Si el número es divisible entre 5, imprimir Buzz
    elif num % 3 == 0:
        # Si el número es divisible entre 3, imprimir Fizz
        print(num, "  Fizz")

        # Si el número es divisible entre 5, imprimir Buzz
    elif num % 5 == 0:
        # Si el número es divisible entre 3, imprimir Fizz
        print(num, "  Buzz")

    else:
        # Si no es divisible entre 3 o 5, imprimir el número
        print(num)
