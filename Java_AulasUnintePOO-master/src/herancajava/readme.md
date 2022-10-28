# Heran�a na Linguagem Java

Tem a premsisa de aproveitar c�digos, j� escritos em uma classe para outras classes. Ou seja, c�digos que servem para mais de uma classe, e com isso evitar repeti��o e re-inser��o de c�difica��o. 

No exmeplo, aproveitaremos metodos e at� atrobutos comuns em ambas as classes. Onde pequenas diferen�as pontuais e exclusivas, diferencia uma classe da outra.

**Evitar dupica��o � uma boa pr�tica. Evita erros e diferen�as em c�digos.**

**extends** + classe " a se clonar", evitamos reescrever novamente c�digos e "c�pia" uma classe alvo e seus atributos.

Exemplo:

<mark> public class LivroDigital extends Livro { </mark>

 No caso, estamos copiando a classe Livros.
 
 Com isso, basta adicionar o que � necess�rio ou exclusivo para esta nova classe, sem precisar reescrever c�digos.
 
 Toda altera��o no c�digo, atributos ou m�todos em Livro, j� � atualizada automaticamente para Livro Digital.
 
 
 **Contrutor e Heran�a**
 
 Se criarmos um construtor na class do qual puxamos as informa��es ( class m�e), teremos tamb�m que criar um construtor nas classes descendentes (filhos(as)). 
 
 Exemplo
 
 __class Livro:__
 
 Criando construtor na classe clonada.

 <mark> public Livro (String autor, String Livro){ } </mark>
 
 __class LivroDigital:__
 
 N�o basta apenas criar uma classe ide^ntica, alterando apenas o nome da classe par a classe atual. temos que usar um atributo chamado **super();**, dentro da classe clone,cos os atributos da classe clonada inserida como par�metro na classe **super**.
 
 Exemplo:
 
  public constructor LivroDigital(){
  
  <mark>super(titulo, autor);</mark>
  
  } 
  
  <cite> Super </cite>: Faz refer�ncia sempre a classe m�e.
  
  
  __Usando palavras reservadas:__
  
  **Super**
  
  Pode mos usar <mark>super</mark> tamab�m apra invocar um metodo da classe m�e. J� que, qusando heran�a, � bem comum existir m�todos com nomes identicos. E usando o <mark>super.</mark> na frente do m�todo, � invocado o m�todo da classe m�e.
  
  Exemplo:
  
<u>System.out.println("Imposto Livro: " +super.imposto());</u>

Usado quando estamos querendo valores de outros m�todos em uma classe diferente da original. PUxando dados da classe m�e, na classe filho(a) por exemplo.
 
 **this**

Usado similar ao _Super_, por�m a refer�ncia � uma class filho(a).

<mark>System.out.println("Imposto Livro: " + this.imposto());</mark>

Por�m, caso a informa��es esteja na mesma classe onde se encontra o m�todo que ela ser� invocada, o _this._ � facultativo.
 
** this. no construtor: **

Aqui, acontece que h� de existir um atributo com o mesmo nomes, e as vezes queremos colcoar esse tributo como um par�metro tamb�m, e causa no sistema uma d�vida de qual atributo est� querendo relacionar. � referente ao atriburo, ou do par�metro? 

Isso por que mesmo nome � usado nos dois casos, e assim temos que informar a qual estamos no referindo: atributo ou par�metro.

_Por padr�o, se estiver dentro de um construtor, ele se refere ao par�metro._

Exemplo no construtor:

<mark> public Livro (String titulo, String autor) </mark>{

	Para n�o haver probelmas, pdoeos simplimente troca o "Titulo" por outro nome, como exemplo "String tl".
	
	Por�m, o nome continuar "titulo" � pertinente para o projeto, logo usamos o **this.** na frente. informando que o nome "String titulo" � um valor que ser� alocado na vari�vel titulo do c�digo;
	
	public Livro (String titulo, String autor){	
		this.titulo = titulo;
	}
}	 


**Uso do m�todo instanceof**

O instanceof � um operador que permite testar se um objeto � uma inst�ncia de um tipo espec�fico de uma class, subclass ou interface.

O instanceof em java tamb�m � conhecida como operador de compara��o de tipos, isso porque compara a inst�ncia com o tipo.

E seu retorno � true (caso a inst�ncia seja do tipo comparado) ou false.
