# Ajuda:

- Static:

Esse artigo Java mostra o uso das variáveis do tipo static, artifício muito usado para manter o controle sobre todos os objetos de uma mesma classe, por exemplo.

Só pelo nome, já dá pra desconfiar que é algo relacionado com constante, algo 'parado' (estático).

Quando definimos uma classe e criamos vários objetos dela, já sabemos que cada objeto irá ser uma cópia fiel da classe, porém com suas próprias variáveis e métodos em lugares distintos da memória.

Ou seja, o objeto 'fusca' tem suas variáveis próprias, diferentes do objeto 'ferrari', embora ambos tenham o mesmo 'modelo', que é a classe 'Carro'.

Quando definimos variáveis com a palavra static em uma classe ela terá um comportamento especial: ela será a mesma para todos os objetos daquela classe.

Ou seja, não haverá um tipo dela em cada objeto. Todos os objetos, ao acessarem e modificarem essa variável, acessarão a mesma variável, o mesmo espaço da memória, e a mudança poderá ser vista em todos os objetos.
