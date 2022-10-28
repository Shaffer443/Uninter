package aula01;

import java.util.Scanner;

/*  Le�nidas � quetionado sobre quantos seus 300 espartanos ir�o enfrantar.
	Fazendo um pequeno jogo de advinha��o, onde o jogador deve dar um palpite.
	Caso seja abaixo ou acima do valor informado o fato.
 	valor correto: 10.000 */

public class aulapratica1_2 {

	public static void main(String[] args) {
		
		System.out.println("Quantos soldados tem o ex�rcito inimido dos Spartanos? ");
		
		Scanner teclado = new Scanner(System.in);
		float inimigos = teclado.nextFloat();
		
		while(inimigos != 10000) {
			
			/* Poderia usar um operador tern�rio:
			 * criar uma vari�vel - String mensagem;
			 * mensagem = inimigos<10000?"UM pouco mais...":"Um pouco Menos...";
			 */
			
			if(inimigos < 10000) {
				System.out.println("Desculpe. Este n�o � o valor correto. Tente novamente.");
				System.out.println("Valor muito baixo, um pouco maior...");
			
			}else{
				
				System.out.println("Desculpe. Este n�o � o valor correto. Tente novamente.");
				System.out.println("Valor muito alto, um pouco menos...");
				
			}
			
			System.out.printf("\nTente Novamente: ");
			inimigos = teclado.nextFloat();			
			
		}
		
		System.out.println("Parab�ns! Este � o valor exato.");
	}

	
}
