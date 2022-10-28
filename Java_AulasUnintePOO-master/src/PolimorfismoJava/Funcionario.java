package PolimorfismoJava;

public class Funcionario {
	
	String nome;

	public Funcionario(String nome) {
		super();
		this.nome = nome;
	}

	public double pagamento() {
		// TODO Auto-generated method stub
		return 0.0f;
	}
	
	/*
	 * Precisamos associar os pagamentos de cada classe a "mãe",q eu é a classe funcionário.
	 * Logo, precisamos criar um método na classe mãe para receber de seus filhos,  informaçês de pagamento
	 * de cada classe. e com isso associar o nome do funcionário ao seu pagemento devido.
	 * 
	 * obs: como todos são double, o pagemtno da classe mãe tem que ser do mesmo tipo.
	 * returno 0.0f, pq não sei o valor a retornar.
	 */
	
	

}
