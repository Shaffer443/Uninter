package aula05_exercicio01;

public class Desktop extends Computador{

	double acessorios;
	
	
	
	public Desktop(int GbMemoria, int numProcessador, double acessorios) {
		super(GbMemoria, numProcessador);
		this.acessorios = acessorios;
	}
	
	


	public double getAcessorios() {
		return acessorios;
	}




	public void setAcessorios(double acessorios) {
		this.acessorios = acessorios;
	}




	@Override
	public double calculaValor() {
		
		return  (GbMemoria * 200) +( NumProcessador*400) + acessorios;
		
	}
	
}
