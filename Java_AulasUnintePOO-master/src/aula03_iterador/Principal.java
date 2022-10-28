package aula03_iterador;

// importando os grupos dos collection

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;

public class Principal {

	public static void main(String[] args) {
		/* 
		 * Para Usar os grupos se escreve o tipo da variável de forma completa,
		 * não apenas sua abrivação. Exemplo: int = integer - <integer>
		 * 
		 */
		
		ArrayList<Integer> lista = new ArrayList ();
		HashSet<Integer> conjunto = new HashSet ();
		HashMap <String, Integer> mapa =  new HashMap();
		
		
		// Passar por todos os elemntos e fazer a soma deles:
		
		int soma;
		soma=0;
		
		for (int i=0; i<lista.size(); i++) {
			
			soma += lista.get(i);
		}
			
			/* 
			 * Abaixo chamamos de for eatch (para cada). Pois não precisa
			 * necessáriamente os indices, pois não interessa. ele ouxa os itens
			 * enquanto existir. Não precisa definir coordenada, tamanho. ele cuida sozinho
			 */
			
			soma = 0;
			
			for (int item: lista) {
				
				soma += item;
				
			}
			
				// Usando iterator = iterator
			
				soma = 0;
				
					//Iterator it = mapa.entrySet().iterator();
					//Iterator it = conjunto.iterator();
					Iterator it = lista.iterator();
					
						while(it.hasNext()) {
							
							soma += (int)it.next();
							
						}
				
			
		}
		

	}


