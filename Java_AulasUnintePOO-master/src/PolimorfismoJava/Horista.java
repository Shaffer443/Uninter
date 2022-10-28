package PolimorfismoJava;

public class Horista extends Funcionario {
	
	int totalhoras;
	float valorhoras;
	
	public Horista(String nome, int totalhoras, float valorhoras) {
		super(nome);
		this.totalhoras = totalhoras;
		this.valorhoras = valorhoras;
	}
	
	public double pagamento() {
		
		return totalhoras*valorhoras;
		
	}
	
	

}
