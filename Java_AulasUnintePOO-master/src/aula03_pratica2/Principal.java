package aula03_pratica2;



public class Principal {
	
	/*
	 * Crie uma classe Aluno com os:
	 * 
	 * Atributos:
	 * 
	 * string nome
	 * int matricula
	 * double desconto
	 * curso curso;
	 * 
	 * métodos:
	 * 
	 * descrever();
	 * pagamento() - Informa o preço que o aluno paga, considerando seu desconto
	 * e o preço de seu curso.
	 * 
	 * E a classe do Curso com os:
	 * 
	 * Atributos:
	 * 
	 * string nome
	 * double mensalidade
	 * 
	 * métodos
	 * 
	 * descrever();
	 * 
	 */

	public static void main(String[] args) {
		
		System.out.println("Sistema de Cobrança");
		System.out.println();
		
		Aluno a1 = new Aluno("Rafael", 001, 150.00, Curso.c1);
		
		a1.info();
		
		
		
		
	}

	

}
