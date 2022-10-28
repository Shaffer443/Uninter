package aula_pratica04_exercicio_02;

public class Ingresso {
	
	public String nomedoevento;
	public double valor;
	
	
	
	
	public Ingresso(String nomedoevento, double valor) {
		
		this.nomedoevento = nomedoevento;
		this.valor = valor;
	}

	

	
	public void imprimir() {
		
		System.out.println("Evento: " + nomedoevento);
		System.out.println("Valor do Ingresso R$ " + valor);
		
		
	}



}
