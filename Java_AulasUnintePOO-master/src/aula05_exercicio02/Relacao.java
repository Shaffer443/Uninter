package aula05_exercicio02;

public class Relacao implements Imprimivel {

	String relacao;
	
	

	public Relacao(String relacao) {
		super();
		this.relacao = relacao;
	}



	@Override
	public void imprimir() {
		
		System.out.println("Relação: " + relacao);
		
	}
	
}
