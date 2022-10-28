package aula05_exercicio02;

public class Ocupacao implements Imprimivel{
	
	String atividade;
	
	

	public Ocupacao(String atividade) {
		super();
		this.atividade = atividade;
	}



	@Override
	public void imprimir() {
		
		System.out.println("Ocupação: " + atividade);
		
	}

}
