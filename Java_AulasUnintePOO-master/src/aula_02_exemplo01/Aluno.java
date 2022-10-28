package aula_02_exemplo01;

public class Aluno {
	
	int matricula;
	String nome;
	String cpf;
	
	Aluno(){
		
		System.out.println(" Novo Cadastro:\n");
	}

	// Criando um método construtor:
	
	Aluno(int pMatricula, String pNome, String pCpf){
		
		matricula= pMatricula;
		nome = pNome;
		cpf = pCpf;
		
	}
	
	
	
	
	// Void porque só mostrará algo na tela. sem nenhum cálculo. 
	void info() { // Método info()
		
		/* Como será executado para vários objetos diferentes, tiramos a referência. 
		 * No caso a ou b, no exemplo.
		 */
		
		System.out.println("Matricula: " + matricula);
		System.out.println("Nome: " + nome);
		System.out.println("CPF: " + cpf);
		System.out.println();
		
	}
}
