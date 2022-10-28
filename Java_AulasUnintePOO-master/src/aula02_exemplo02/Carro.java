package aula02_exemplo02;

public class Carro {
	
	String nome;
	String modelo;
	float autonomia;
	
	
	// Criando um MÉTODO STATIC :
	// Objetivo em transformar milhas em metros.
	
	static float MilharParaMetros(float milhas) {
		//(float milhas) - variável recebida para ação.
		
		return milhas*1600;
	}
	
	// Criando um ATRIBUTO Static:
	
	static final double PI = 3.1415;
	
	/* Adicionando a palavra FINAL, a váriável não se altera. Mesmo que 
	 * a codificação solicite esta alteraçãod e valor.
	 */
	
	void info() {
		
	
	System.out.println("Nome: " + nome);
	System.out.println("Modelo: " + modelo);
	System.out.println("Velocidade: " + autonomia);
	System.out.println("Distância em Metros: " + MilharParaMetros(autonomia));
	
	}

}
