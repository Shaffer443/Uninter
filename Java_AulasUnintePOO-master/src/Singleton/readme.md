# Ajuda:

- Static:

Esse artigo Java mostra o uso das vari�veis do tipo static, artif�cio muito usado para manter o controle sobre todos os objetos de uma mesma classe, por exemplo.

S� pelo nome, j� d� pra desconfiar que � algo relacionado com constante, algo 'parado' (est�tico).

Quando definimos uma classe e criamos v�rios objetos dela, j� sabemos que cada objeto ir� ser uma c�pia fiel da classe, por�m com suas pr�prias vari�veis e m�todos em lugares distintos da mem�ria.

Ou seja, o objeto 'fusca' tem suas vari�veis pr�prias, diferentes do objeto 'ferrari', embora ambos tenham o mesmo 'modelo', que � a classe 'Carro'.

Quando definimos vari�veis com a palavra static em uma classe ela ter� um comportamento especial: ela ser� a mesma para todos os objetos daquela classe.

Ou seja, n�o haver� um tipo dela em cada objeto. Todos os objetos, ao acessarem e modificarem essa vari�vel, acessar�o a mesma vari�vel, o mesmo espa�o da mem�ria, e a mudan�a poder� ser vista em todos os objetos.
