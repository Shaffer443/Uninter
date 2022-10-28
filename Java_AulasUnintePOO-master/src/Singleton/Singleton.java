package Singleton;

public class Singleton {
	
	public int numero;
	private static Singleton instancia = null;
	
	private Singleton() {
		
		numero = 20;
	}
	
	public static Singleton getInstance() {
		if(instancia == null){
			
			instancia = new Singleton();
			
		}
		
		return instancia;
	}
	
	/*
	 * assim declaramos que o get Instance(), vai decalrar a mesma instâcnia ao longo de todo o projeto. 
	 */

}
