package aula02_exemplo02;

public class Carro {
	
	String nome;
	String modelo;
	float autonomia;
	
	
	// Criando um M�TODO STATIC :
	// Objetivo em transformar milhas em metros.
	
	static float MilharParaMetros(float milhas) {
		//(float milhas) - vari�vel recebida para a��o.
		
		return milhas*1600;
	}
	
	// Criando um ATRIBUTO Static:
	
	static final double PI = 3.1415;
	
	/* Adicionando a palavra FINAL, a v�ri�vel n�o se altera. Mesmo que 
	 * a codifica��o solicite esta altera��od e valor.
	 */
	
	void info() {
		
	
	System.out.println("Nome: " + nome);
	System.out.println("Modelo: " + modelo);
	System.out.println("Velocidade: " + autonomia);
	System.out.println("Dist�ncia em Metros: " + MilharParaMetros(autonomia));
	
	}

}
