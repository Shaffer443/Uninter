package aula03_collection;

// Importação necessária para trabalhar com ArrayList
import java.util.ArrayList;

//Importação necessária para trabalhar com LinkedList
import java.util.LinkedList;

//Importação necessária para trabalhar com HashMap
import java.util.HashMap;

//Importação necessária para trabalhar com os métodos do collections
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
		
		//Removendo o 4 itém da lista de pessoas
		
		System.out.println(pessoas.remove(3));
		
		// Usando um método do API Collection:
		// Ordenando a lista/objetos:
		
		/*Adicionando mais um elemento na posiçaõ removida */
		
		pessoas.add("Barney");
		
		Collections.sort(pessoas);
		System.out.println(pessoas);// imprime em ordem
		
		// Ordenando aleatóriamente a lista/objetos:
		
				Collections.shuffle(pessoas);
				System.out.println(pessoas);// imprime em ordem aleatória
				
				// Ordenando reversamente a lista/objetos:
				
				Collections.reverse(pessoas);
				System.out.println(pessoas);// imprime em ordem reversa em relação ao shuffle, neste caso. pois está antes

		/* 
		 * OBS: Usando o sysout(e o código do parêmetro), ação é mostrada, impressa
		 * mas não executada de fato. como uma simulação.
		 * Para executar, usar o código fora do sysout
		 * exemplo: pessoas.remove(4);
		 * 
		 */
		
		
		// Usando o MAP:
		// Povoando com duas String's
		
		HashMap<String, String> capitais = new HashMap();
		
		
		/* 
		 * Para a chave Pernmabuco, temos Recife. Para a chave Paraíba, temos João Pessoa.
		 */
		
		capitais.put("Pernambuco", "Recife");
		capitais.put("Paraíba", "João Pessoa");
		capitais.put("Rio Grande do Norte", "Natal");
		capitais.put("Alagoas", "Maceió");
		capitais.put("Bahia", " Salvador");
		capitais.put("Sergipe", "Aracajú");
		capitais.put("Ceára", "Fortaleza");
		
		System.out.println();
		
		// Informa as chaves e seu contaúdo:
		System.out.println(capitais);
		
		// Indicando a chave é informado o valor:
		System.out.println(capitais.get("Bahia"));
		
		/* Com o MAP é bem mais rápido esse tipo de busca */
		
		
		
	}

}
