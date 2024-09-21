# livros [ didático, poesia, ficção, auto-ajuda, economia]

'''
O livro é de fácil leitura? (Nota de 0 a 5)
O livro é difícil? (Nota de 0 a 5)
O livro é cheio de fórmulas? (Nota de 0 a 5)
O livro contém rimas? (Nota de 0 a 5)
O livro é utópico? (Nota de 0 a 5)
'''

from sklearn.neighbors import KNeighborsClassifier
livro1 = [0, 5, 5, 0, 0]
livro2 = [0, 5, 0, 0, 0]
livro3 = [5, 5, 0, 0, 0]
livro4 = [0, 0, 5, 5, 0]
isDidatico = [0, 1, 1, 0]  # as classes que sõ atribuídas ao livro didático

x = [livro1, livro2, livro3, livro4]
y = isDidatico


neigh = KNeighborsClassifier(n_neighbors=3)

neigh.fit(x, y)

novoLivro = [[4, 4, 4, 4, 4]]
result = neigh.predict(novoLivro)
print(result)

if result == 0:
    print('É didático')
else:
    print('Não é didático')
