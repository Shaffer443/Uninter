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
	 * m�todos:
	 * 
	 * descrever();
	 * pagamento() - Informa o pre�o que o aluno paga, considerando seu desconto
	 * e o pre�o de seu curso.
	 * 
	 * E a classe do Curso com os:
	 * 
	 * Atributos:
	 * 
	 * string nome
	 * double mensalidade
	 * 
	 * m�todos
	 * 
	 * descrever();
	 * 
	 */

	public static void main(String[] args) {
		
		System.out.println("Sistema de Cobran�a");
		System.out.println();
		
		Aluno a1 = new Aluno("Rafael", 001, 150.00, Curso.c1);
		
		a1.info();
		
		
		
		
	}

	

}
