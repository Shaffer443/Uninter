package aula_02_exemplo01;

public class Aluno {
	
	int matricula;
	String nome;
	String cpf;
	
	Aluno(){
		
		System.out.println(" Novo Cadastro:\n");
	}

	// Criando um m�todo construtor:
	
	Aluno(int pMatricula, String pNome, String pCpf){
		
		matricula= pMatricula;
		nome = pNome;
		cpf = pCpf;
		
	}
	
	
	
	
	// Void porque s� mostrar� algo na tela. sem nenhum c�lculo. 
	void info() { // M�todo info()
		
		/* Como ser� executado para v�rios objetos diferentes, tiramos a refer�ncia. 
		 * No caso a ou b, no exemplo.
		 */
		
		System.out.println("Matricula: " + matricula);
		System.out.println("Nome: " + nome);
		System.out.println("CPF: " + cpf);
		System.out.println();
		
	}
}
