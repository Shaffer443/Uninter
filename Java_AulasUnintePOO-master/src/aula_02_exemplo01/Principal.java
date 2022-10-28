package aula_02_exemplo01;

public class Principal {

	public static void main(String[] args) {
		
		System.out.println("Relatório de Cadastros\n");
		Aluno a = new Aluno();
		a.matricula=1001;
		a.nome="Rafael Gouveia";
		a.cpf="111222333-44";		
		
		System.out.println("Matricula: " + a.matricula);
		System.out.println("Nome: " + a.nome);
		System.out.println("CPF: " + a.cpf);
		
		System.out.println();
		
		// Criando e povoando os dados.
		
		Aluno b = new Aluno();
		b.nome="Pollyanna Maia";
		b.cpf="222333444-55";
		b.matricula=1002;
		
		
		System.out.println("Matricula: " + b.matricula);
		System.out.println("Nome: " + b.nome);
		System.out.println("CPF: " + b.cpf);
		System.out.println();
		
		// Povoando em uma só linha
		
		Aluno x = new Aluno(1010, "Barney", "666.555.444-89"); 
		
		x.info();
		
		/* Não tem o ALuno ();, por isso não imprimiu nada.*/
		
		// Alterando um nome:
		System.out.println();
		
		a.nome = "Giovanna";
		
		System.out.println("Matricula: " + a.matricula);
		System.out.println("Nome: " + a.nome);
		System.out.println("CPF: " + a.cpf);
		System.out.println();
		
		/* Replicando. Porém não é profissional replicar.
		 * Para resolver, criamos um método.
		 */
		
		// Chamando os dados já com o método criado.
		
		a.info();
		
		// modificação:
		a.nome = "Edilene Gouveia";
		
		a.info();
		
		b.nome = "Teobaldo Melo";
		
		b.info();
		
		
		
		
	}

}
