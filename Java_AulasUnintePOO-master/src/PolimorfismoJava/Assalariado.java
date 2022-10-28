package PolimorfismoJava;

public class Assalariado extends Funcionario {
	
	float salario;

	public Assalariado(String nome, float salario) {
		super(nome);
		this.salario = salario;
	}
	
	
	public double pagamento() {
		
		return salario;
		
	}
	

}
