package aula05_exercicio01;

import java.util.ArrayList;

public class Principal {

	public static void main(String[] args) {
		
		Computador loja [] = { new Desktop (4, 1, 600), new Notebook(8, 2, 22)};
		Computador site [] = { new Desktop (16, 4, 200), new Notebook(4, 1, 17)};
		
		
		//Criando por lista de Arraylist:
		
		
		ArrayList<Computador> ListaCompras = new ArrayList();
		
		ListaCompras.add(new Desktop(16,8,1200)); //Adiciona novos intens, por exemplo.
		ListaCompras.add(new Notebook(16,4,27)); //Adiciona novos intens, por exemplo.
		
		float ListaTotal=0;
		
		for(Computador c : ListaCompras) {
			
			ListaTotal += c.calculaValor();
			
		}
		
		
		float TotalSite = 0;
		float TotalLoja = 0;
		
		Computador compra; // Ponteiro, referência para computador
		
		/*
		 * Criamos a referencia apra Computador pq o calculaValor está dentro da classe mãe Computador.
		 */
		
		for (int i=0; i<loja.length; i++) {
			
			compra = loja[i];
			
			System.out.println("Total de Memorias vendidas: " + compra.GbMemoria);
			System.out.println("Total de Processadores vendidos: " + compra.NumProcessador);
			//System.out.println("Total de Processadores vendidos: " + acessorios);
			
			TotalLoja += compra.calculaValor();
			
		}
		
		System.out.println();
		System.out.println("R$ " +TotalLoja);
		System.out.println("-------------------------------------------------------------------------");
		
		for (int i=0; i<site.length; i++) {
			
			compra = site[i];
			
			System.out.println("Total de Memorias vendidas: " + compra.GbMemoria);
			System.out.println("Total de Processadores vendidos: " + compra.NumProcessador);
			//System.out.println("Total de Processadores vendidos: " + Notebook.getPolegadasTela());
			
			TotalSite += compra.calculaValor();
			
		}
		
		System.out.println();
		System.out.println("R$ " + TotalSite);
		System.out.println("-------------------------------------------------------------------------");

		float TotalVendas = TotalSite + TotalLoja + ListaTotal;
		
		System.out.println("Total Geral da Vendas R$ " + TotalVendas );
		
	}

}
