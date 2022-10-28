package PolimorfismoJava;

public class Comissionado extends Funcionario {
	
	float comissao;
	float vendas;
	
	
	public Comissionado(String nome, float comissao, float vendas) {
		super(nome);
		this.comissao = comissao;
		this.vendas = vendas;
	}
	
	public double pagamento() {
		
		return vendas*comissao;
		
	}
	

}
