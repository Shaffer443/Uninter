# Livraria

Cria��o de diversas classes (class), onde a intera��o entre as classes, atrav�s do uso de _extends_ e _super()_.

codifica��es de intera��o entre void's:

@Override //informa ao compilador que h� um subescri��o ao sistema.
	public void info() {
		
		super.info(); // super faz refer�ncia a classe m�e.
		System.out.println("N� da tiragem: " + tiragem);
		System.out.println("Peso: " + peso + " g");
		
	} 
	
Codifica��o principal (Instanciando):

<mark>LivroDigital ld1 = new LivroDigital("Silmarilion", new Autor("R.R.Tolkien", " null ", "Reino Unido"),"Aventura | Fantasia", 5, 430, 3500);</mark>

<Class Alvo> <nome dado> = new <Class alvo usada> ("titulo", <cria��o do novo autor>("autor","email","nacionalidade"),"genero","edi��o","download","tamanho do arquivo (mb)")