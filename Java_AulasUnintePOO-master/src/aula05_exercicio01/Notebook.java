package aula05_exercicio01;

public class Notebook extends Computador {
	
	
	int polegadasTela;
	
	
	
	public Notebook(int GbMemoria, int numProcessador, int polegadasTela) {
		super(GbMemoria, numProcessador);
		this.polegadasTela = polegadasTela;
	}
	
	


	public  int getPolegadasTela() {
		return polegadasTela;
	}




	public void setPolegadasTela(int polegadasTela) {
		this.polegadasTela = polegadasTela;
	}




	@Override
	public double calculaValor() {
		
		return (GbMemoria*250) + (NumProcessador * 500) + (polegadasTela*100);
		
	}

}
