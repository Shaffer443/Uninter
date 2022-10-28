package Cofrinho;

public class Principal {

	public static void main(String[] args) {
		
		Cofrinho porquinho = new Cofrinho();
		
		porquinho.add(new Moeda("Real", 0.50));
		porquinho.add(new Moeda("Real", 0.10));
		porquinho.add(new Moeda("Real", 0.05));
		porquinho.add(new Moeda("Real", 0.25));
		porquinho.add(new Moeda("Real", 1.00));
		
		System.out.printf("Saldo total do porquinho: R$ %.2f", porquinho.Total());
		
		// PRINTF não usa-se "+" e sim ","
	}

}
