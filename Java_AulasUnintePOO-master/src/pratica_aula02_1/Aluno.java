package pratica_aula02_1;

import java.util.Scanner;

public class Aluno {

	String nome, curso;
	double nota1,nota2, nota3;
	
	Scanner Teclado = new Scanner(System.in);
	
	
	
	Aluno(){
		
		System.out.println("Digite o Nome aluno(a): ");
		nome = Teclado.next();
		System.out.println("Digite o Curso aluno(a): ");
		curso = Teclado.next();
		
		System.out.println("Aluno(a): " + nome + ", foi cadastrada com sucesso no curso de " + curso);
		System.out.println();
		
		
		info();
			
		}
	

	
	public Aluno(String nome, String curso) {
		
		this.nome = nome;
		this.curso = curso;
		
	}

	public double Avaliacao() {
		
		System.out.println("Digite as três notas do aluno(a)(Use virgula(,): " + nome);
		
		nota1 = Teclado.nextDouble();
		nota2 = Teclado.nextDouble();
		nota3 = Teclado.nextDouble();
			
		return (nota1 + nota2 + nota3)/3;
		
	}
	
	void info() {
		
		System.out.println("Resultado:");
		System.out.println("O aluno(a) "+ nome + ", tem a média de " + Avaliacao() + ", no curso de " + curso);
		System.out.println();
		
	}
	
}
