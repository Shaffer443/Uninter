package herancajava;

public class Principal {

	public static void main(String[] args) {
		// Instanciando exemplos:
		
		Livro obra1 = new Livro("Silmarilion", "Tolkien");
		
		obra1.imposto();
		
		System.out.println(obra1.imposto());
		
		
		LivroDigital obra2 = new LivroDigital ("Silmarilion", "Tolkien", "http://www.silmarilion.com");
		
		obra2.imposto();
		
		System.out.println(obra2.imposto());
		
		
		// Usando instanceof, verificamos se determinada classe é instanciada (faz parte, é clone ou cópia), de uma determinada outra classe.
		
		System.out.println();
		System.out.println(obra1 instanceof Livro);
		System.out.println(obra2 instanceof Livro);
		System.out.println(obra1 instanceof LivroDigital);
		System.out.println(obra2 instanceof LivroDigital);
		
		
		// retorna se é true (verdadeiro), ou false.
		
		
		
		
		
		
	}

}
