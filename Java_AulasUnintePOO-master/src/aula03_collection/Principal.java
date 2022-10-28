package aula03_collection;

// Importa��o necess�ria para trabalhar com ArrayList
import java.util.ArrayList;

//Importa��o necess�ria para trabalhar com LinkedList
import java.util.LinkedList;

//Importa��o necess�ria para trabalhar com HashMap
import java.util.HashMap;

//Importa��o necess�ria para trabalhar com os m�todos do collections
import java.util.Collections;

public class Principal {

	public static void main(String[] args) {
		
		/* Exemplo de uso da API Collection */
		
		// Modelo ArrayLista:
		//ArrayList<String> pessoas = new ArrayList();
		
		// Modelo LinkedList:
		LinkedList<String> pessoas = new LinkedList();
		
		pessoas.add("Rafael");
		pessoas.add("Polly");
		pessoas.add("Giovana");
		pessoas.add("Barney");
		
		// Devolve os elemnto adcionado na lista pessoas acima.
		// passando o nome da lista. No caso, pessoas.
		
		System.out.println(pessoas);
		
		//Acessando a primeira pessoas da lista
		
		System.out.println(pessoas.get(0));
		
		//Removendo o 4 it�m da lista de pessoas
		
		System.out.println(pessoas.remove(3));
		
		// Usando um m�todo do API Collection:
		// Ordenando a lista/objetos:
		
		/*Adicionando mais um elemento na posi�a� removida */
		
		pessoas.add("Barney");
		
		Collections.sort(pessoas);
		System.out.println(pessoas);// imprime em ordem
		
		// Ordenando aleat�riamente a lista/objetos:
		
				Collections.shuffle(pessoas);
				System.out.println(pessoas);// imprime em ordem aleat�ria
				
				// Ordenando reversamente a lista/objetos:
				
				Collections.reverse(pessoas);
				System.out.println(pessoas);// imprime em ordem reversa em rela��o ao shuffle, neste caso. pois est� antes

		/* 
		 * OBS: Usando o sysout(e o c�digo do par�metro), a��o � mostrada, impressa
		 * mas n�o executada de fato. como uma simula��o.
		 * Para executar, usar o c�digo fora do sysout
		 * exemplo: pessoas.remove(4);
		 * 
		 */
		
		
		// Usando o MAP:
		// Povoando com duas String's
		
		HashMap<String, String> capitais = new HashMap();
		
		
		/* 
		 * Para a chave Pernmabuco, temos Recife. Para a chave Para�ba, temos Jo�o Pessoa.
		 */
		
		capitais.put("Pernambuco", "Recife");
		capitais.put("Para�ba", "Jo�o Pessoa");
		capitais.put("Rio Grande do Norte", "Natal");
		capitais.put("Alagoas", "Macei�");
		capitais.put("Bahia", " Salvador");
		capitais.put("Sergipe", "Aracaj�");
		capitais.put("Ce�ra", "Fortaleza");
		
		System.out.println();
		
		// Informa as chaves e seu conta�do:
		System.out.println(capitais);
		
		// Indicando a chave � informado o valor:
		System.out.println(capitais.get("Bahia"));
		
		/* Com o MAP � bem mais r�pido esse tipo de busca */
		
		
		
	}

}
