package aula01;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class aulapratica1_3 {

	/* Leia uma seguencia de N strings e as imprima em ordem reversa. Utilize um método */
	
	
	public static void main(String[] args) {
		
		ArrayList<String> nomes = new ArrayList(); // criação do Array
		Scanner entrada = new Scanner(System.in); // criação do teclado(input, entrada)
		
		String texto; // variável para temporária, auxiliando na leitura dos dados( texto, msg, letras)
		
		// Informa o tamanho, primario da lista:
		System.out.println("Digite a quantidade de nomes a ser inserido na lista: ");
		int total = entrada.nextInt(); // // lendo a quantidade de string decalrada a ser inserida
				
		
		System.out.println("Digite os nomes: "); //nomes a serem inseridos na lista.
		
		/* Usa-se o sinal de "<" e não o de "<=", devido a uma lista ter o zero ( 0 ), como o primeiro itém,
		 * assim, como o zero conta, não pode ser igual ao "total" neste exemplo. precisa ser menor. 
		 */
		for(int i=0; i<total;i++) {
			
			texto = entrada.next(); // lê o texto. 
			nomes.add(texto); // add o texto.
			
			/* outro modo de se fazer a contagem:
			
			nome.add(entrada.next()); // add letras, nomes na lista
			
			*/
		}
		System.out.printf("\nOrdem Normal:");
		System.out.println(nomes);
		
		System.out.printf("\nOrdem Reversa:");
		Collections.reverse(nomes);
		System.out.println(nomes);
		
		
	}

}
