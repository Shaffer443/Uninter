package aula01;

import java.util.Scanner;

public class aula01 {

	public static void main(String[] args) {
		System.out.println("Hello World!"); //Print na tela
		System.out.println("# Usa prâmetros da Liguagem C ");
		System.out.println("");
		
		int idade=37; // Declarando um inteiro.
		float peso; // Declarando um float.
		String nome2; //declarando uma String (apenas me JAVA).
		// char nome2; também pode ser usado em algumas situações.
		int cep;
		
		
		String nome = "Rafael";
		int tamanho = nome.length(); //variavel.length();
		System.out.printf("Total de letras em %s: %d ",nome, tamanho); // imprimindo variável com a contagem
		nome2 = nome + " Gouveia"; //Concatenação 
		System.out.println("\n"+ nome2);  
		
		//arrays:
		
		int[] megasena = {03,05,11,27,37,52}; // pode-se usar o [] antes ou depois do megasena.
		
		System.out.println(megasena.length); // lendo o array megasena e contando seu conteudo.
		
		//int quina = new int[5]; // solicitando ao sistema um espaço de memoria para 5 alocações
		
		//Solicitando entrada do usuário:
		
		System.out.println("Digite seu CEP: ");
		
		Scanner teclado = new Scanner(System.in);
		
		cep = teclado.nextInt(); // A vatiável precisa se conectar com o "in" para receber valor
		
		System.out.println("Seu CEP é: " + cep);

	}

}
