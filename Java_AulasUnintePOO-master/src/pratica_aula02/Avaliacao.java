package pratica_aula02;

import java.util.Scanner;

public class Avaliacao {

	String nome;
	double nota1, nota2, nota3;
	double mediaa;
	double mediap1, mediap2, mediap3;
	
	
	Scanner Teclado = new Scanner (System.in);
	
	// Construtor modelo 1:
	
	Avaliacao(){
		
		
		System.out.println("Digite o nome do Aluno(a): ");
		nome = Teclado.next();
		System.out.println("Digite a Primeira nota do Aluno(a) " + nome + ": ");
		nota1= Teclado.nextFloat();
		System.out.println("Digite a Segunda nota do Aluno(a) " + nome + ": ");
		nota2= Teclado.nextFloat();
		System.out.println("Digite a Terceira nota do Aluno(a) " + nome + ": ");
		nota3= Teclado.nextFloat();
		
		
	}
	
	// Construtor modelo 2:
	
	Avaliacao(String nome, double nota1, double nota2, double nota3){
		
		this.nome = nome;
		this.nota1= nota1;
		this.nota2= nota2;
		this.nota3= nota3;
		
	}
	
	
	public double MediaAritmetica() {
		
		mediaa = (nota1 + nota2 + nota3)/3;
		
		return mediaa;
		
	}
	
	public double MediaPonderada() {
		
		mediap1 = nota1 * 2;
		mediap2 = nota2 * 3;
		mediap3 = nota3 * 4;
		
		
		return (mediap1+mediap2+mediap3)/9;
		 
	}
	
	public double MediaGeral() {
		
		
		
		return (MediaAritmetica() + MediaPonderada())/2;
		 
	}
	
	void info() {
		
		System.out.println("Médias do Aluno: " + nome);
		System.out.printf("Média Aritmética -  " + MediaAritmetica() + " \n" );
		System.out.println("Média Ponderada - " + MediaPonderada());
		System.out.println("Média Geral =  " + MediaGeral());
		System.out.println();
		
		
		
	}
	
	
	
	
}
