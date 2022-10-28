package aula05_exercicio01;

public abstract class Computador {
	
	int GbMemoria;
	int NumProcessador;
	
	
	
	public Computador(int GbMemoria, int numProcessador) {
		this.GbMemoria = GbMemoria;
		NumProcessador = numProcessador;
	}



	public abstract double calculaValor();

}
