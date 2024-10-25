def fibonacci(num):
    #inicio com dois primeiros numeros
    a, b = 0, 1
    
    while b < num:
        a, b = b, a + b

    if b == num or num == 0:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} não pertence à sequência de Fibonacci."


num = int(input("Informe um número: "))
print(fibonacci(num))