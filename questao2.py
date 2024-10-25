def quantity(string):

    total = string.count('a')

    if total > 0:
        return f"A letra 'a' aparece {total} vez(es) na string."

    else:
        return "A letra 'a' não está presente na string."

string = input("Digite uma string: ").lower()
resultado = quantity(string)
print(resultado)