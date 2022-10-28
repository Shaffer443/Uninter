package aula_pratica04_exercicio_01;

public class Principal {

	public static void main(String[] args) {
		
		//new Autor(seu parâmetros)
		
		LivroDigital ld1 = new LivroDigital("Silmarilion", new Autor("R.R.Tolkien", " null ", "Reino Unido"),"Aventura | Fantasia", 5, 430, 3500);
	
		ld1.info();
	
	}
}
