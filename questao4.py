"""
a) 
7 - 5 = 2
5 - 3 = 2
3 - 1 - 2
logo ...

B)
2 x 2 = 4
4 x 2 = 8
8 x 2 = 16
logo...

C)
0^2 = 0
1^2 = 1
2^2 = 4
3^2 = 9
4^2 = 16

logo...

D) mesma lógica acima porém somente os pares
E) sequência de fibonacci somando os dois ultimos elementos
F) é uma charada que precisei pesquisar, a resposta é 200 pois todos os numeros começam com a letra D
"""
list_a = [1, 3, 5, 7]
next_a = list_a[-1] + 2  
print("Próximo elemento da lista A:", next_a)

list_b = [2, 4, 8, 16, 32, 64]
next_b = list_b[-1] * 2 
print("Próximo elemento da lista B:", next_b)

list_c = [0, 1, 4, 9, 16, 25, 36]
next_c = (len(list_c))**2  
print("Próximo elemento da lista C:", next_c)

list_d = [4, 16, 36, 64]
next_d = ((len(list_d) + 1) * 2)**2  # quadrado perfeito par
print("Próximo elemento da lista D:", next_d)

list_e = [1, 1, 2, 3, 5, 8]
next_e = list_e[-1] + list_e[-2]  # soma dos dois últimos elementos
print("Próximo elemento da lista E:", next_e)

