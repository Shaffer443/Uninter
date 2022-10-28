package aula01;

import java.util.Scanner;

// Obtenha a entrada padrão peso (int), altura (double) e imprimir o IMC.
// IMC: peso em quilogramas dividido pela altura em metros elevada ao quadrado.
// IMC = PESO / ALTURA ao quadrado.

public class aulapratica1 {

	public static void main(String[] args) {
		
		System.out.println("Digite Seu Peso (kg): ");
		Scanner teclado = new Scanner(System.in);

		float peso = teclado.nextFloat();
		
		System.out.println("Digite sua altura (m): ");
		
		float altura = teclado.nextFloat();
		
		float imc = (int) peso /(altura*altura);
		
		System.out.printf("Seu IMC é: %.2f", imc);
	}

}
