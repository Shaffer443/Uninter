package aula05_exercicio02;

public class Familia implements Imprimivel {
	
	String nome;
	String sobrenome;
	
	
	
	public Familia(String nome, String sobrenome) {
		super();
		this.nome = nome;
		this.sobrenome = sobrenome;
	}



	@Override
	public void imprimir() {
		
		System.out.println("Nome: " + nome + " " + sobrenome);
		
	}
	

}
