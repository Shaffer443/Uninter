# Herança na Linguagem Java

Tem a premsisa de aproveitar códigos, já escritos em uma classe para outras classes. Ou seja, códigos que servem para mais de uma classe, e com isso evitar repetição e re-inserção de códificação. 

No exmeplo, aproveitaremos metodos e até atrobutos comuns em ambas as classes. Onde pequenas diferenças pontuais e exclusivas, diferencia uma classe da outra.

**Evitar dupicação é uma boa prática. Evita erros e diferenças em códigos.**

**extends** + classe " a se clonar", evitamos reescrever novamente códigos e "cópia" uma classe alvo e seus atributos.

Exemplo:

<mark> public class LivroDigital extends Livro { </mark>

 No caso, estamos copiando a classe Livros.
 
 Com isso, basta adicionar o que é necessário ou exclusivo para esta nova classe, sem precisar reescrever códigos.
 
 Toda alteração no código, atributos ou métodos em Livro, já é atualizada automaticamente para Livro Digital.
 
 
 **Contrutor e Herança**
 
 Se criarmos um construtor na class do qual puxamos as informações ( class mãe), teremos também que criar um construtor nas classes descendentes (filhos(as)). 
 
 Exemplo
 
 __class Livro:__
 
 Criando construtor na classe clonada.

 <mark> public Livro (String autor, String Livro){ } </mark>
 
 __class LivroDigital:__
 
 Não basta apenas criar uma classe ide^ntica, alterando apenas o nome da classe par a classe atual. temos que usar um atributo chamado **super();**, dentro da classe clone,cos os atributos da classe clonada inserida como parâmetro na classe **super**.
 
 Exemplo:
 
  public constructor LivroDigital(){
  
  <mark>super(titulo, autor);</mark>
  
  } 
  
  <cite> Super </cite>: Faz referência sempre a classe mãe.
  
  
  __Usando palavras reservadas:__
  
  **Super**
  
  Pode mos usar <mark>super</mark> tamabém apra invocar um metodo da classe mâe. Já que, qusando herança, é bem comum existir métodos com nomes identicos. E usando o <mark>super.</mark> na frente do método, é invocado o método da classe mãe.
  
  Exemplo:
  
<u>System.out.println("Imposto Livro: " +super.imposto());</u>

Usado quando estamos querendo valores de outros métodos em uma classe diferente da original. PUxando dados da classe mãe, na classe filho(a) por exemplo.
 
 **this**

Usado similar ao _Super_, porém a referência é uma class filho(a).

<mark>System.out.println("Imposto Livro: " + this.imposto());</mark>

Porém, caso a informações esteja na mesma classe onde se encontra o método que ela será invocada, o _this._ é facultativo.
 
** this. no construtor: **

Aqui, acontece que há de existir um atributo com o mesmo nomes, e as vezes queremos colcoar esse tributo como um parâmetro também, e causa no sistema uma dúvida de qual atributo está querendo relacionar. É referente ao atriburo, ou do parâmetro? 

Isso por que mesmo nome é usado nos dois casos, e assim temos que informar a qual estamos no referindo: atributo ou parâmetro.

_Por padrão, se estiver dentro de um construtor, ele se refere ao parâmetro._

Exemplo no construtor:

<mark> public Livro (String titulo, String autor) </mark>{

	Para não haver probelmas, pdoeos simplimente troca o "Titulo" por outro nome, como exemplo "String tl".
	
	Porém, o nome continuar "titulo" é pertinente para o projeto, logo usamos o **this.** na frente. informando que o nome "String titulo" é um valor que será alocado na variável titulo do código;
	
	public Livro (String titulo, String autor){	
		this.titulo = titulo;
	}
}	 


**Uso do método instanceof**

O instanceof é um operador que permite testar se um objeto é uma instância de um tipo específico de uma class, subclass ou interface.

O instanceof em java também é conhecida como operador de comparação de tipos, isso porque compara a instância com o tipo.

E seu retorno é true (caso a instância seja do tipo comparado) ou false.
