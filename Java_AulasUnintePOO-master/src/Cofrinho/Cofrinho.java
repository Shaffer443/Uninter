package Cofrinho;

import java.util.ArrayList;

public class Cofrinho {

//Melhor modo, como não sabemos o tamanho é usar lista.
	//atalho de importação de bibliotecas: crtl+shift+ O 
	
	private ArrayList<Moeda> moedas = new ArrayList();
	
	/*
	 * Metodo add - Toda vez que recebe uma moeda (m), adiciona uma moeda.
	 *  Quando chama o metodo adionas do cofrinho, vai achamar o add do valor arraylist moedas.
	 */
	
	void add(Moeda m) {
		
		moedas.add(m);
	}


	// Recuperando o total:
	
	public double Total() {
		
		double total =0;
		
		
		 // for vai varrer toda a listad e moedas, e pegando os valores alocados.
		 
		
		for(Moeda m : moedas) {
			
			total += m.getValor();
			
			/*
			 * podemos incremenatr ainda, onde o tipo da moeda será
			 * multiplicado pelo valro da cotação do dia.
			 */
			
		}
		
		return total;
	}
	
	
	
}
