# Livraria

Criação de diversas classes (class), onde a interação entre as classes, através do uso de _extends_ e _super()_.

codificações de interação entre void's:

@Override //informa ao compilador que há um subescrição ao sistema.
	public void info() {
		
		super.info(); // super faz referência a classe mãe.
		System.out.println("Nº da tiragem: " + tiragem);
		System.out.println("Peso: " + peso + " g");
		
	} 
	
Codificação principal (Instanciando):

<mark>LivroDigital ld1 = new LivroDigital("Silmarilion", new Autor("R.R.Tolkien", " null ", "Reino Unido"),"Aventura | Fantasia", 5, 430, 3500);</mark>

<Class Alvo> <nome dado> = new <Class alvo usada> ("titulo", <criação do novo autor>("autor","email","nacionalidade"),"genero","edição","download","tamanho do arquivo (mb)")