package aula03_pratica;

/* 
 * Exerc�cio consiste me cria uma Classe nota com dois atributos privados:
 * double nota 1
 * double nota 2
 * 
 * Cinco m�todos p�blicos:
 * 
 * void setNota1(double);
 * void setNota2(double);
 * double getNota1()
 * double getNota2()
 * 
 * void resultado()
 * 
 * O m�todo resultado() deve imprimir a m�dia e se o aluno est� aprovado,
 * reprovado ou de final. no caso de estar na final, o quando de nota precisa na final.
 */

/* 
 * fase 2:
 * 
 * Adicionar o atributo "faltas". no resulatdo, para quem tiver acima de 7 faltas, imprimir
 * "reprovado pro faltas".
 * */

public class Nota {
	
	
	private double nota1;
	private double nota2;
	private double situacao;
	private double recuperacao;
	private int faltas;
	
	
	// construtor:
	
	Nota( double nota1, Double nota2, int faltas){
		
		this.nota1 = nota1;
		this.nota2 = nota2;
		this.faltas = faltas;
		
		
	}
	
	//Nota (double Nota1, double nota2);
	
	public double getNota1() {
		return nota1;
	}
	public void setNota1(double nota1) {
		this.nota1 = nota1;
	}
	public double getNota2() {
		return nota2;
	}
	public void setNota2(double nota2) {
		this.nota2 = nota2;
	}
	
		
		public int getFaltas() {
		return faltas;
	}

	public void setFaltas(int faltas) {
		this.faltas = faltas;
	}

	
	
	
	void resultado() {
		
		
		
		System.out.println("Primeira Nota: " + nota1);
		System.out.println("Segunda Nota: " + nota2);
		
		if(faltas>7) {
			
			System.out.println("Reprovado por faltas. (total "+faltas+")");
			
		
		}else {
			
			
			situacao = (nota1+nota2)/2;
			recuperacao = 14 - situacao;
			
			if(situacao < 7.0) {
				
				
				
				System.out.println("Sua m�dia foi " + situacao + ", e precisa de " + recuperacao + ", para ser aprovado.");
				
				
			} else {
				
				System.out.println("Parab�ns! sua m�dia foi " + situacao + ". Voc� foi aprovado com sucesso!");
				
			}
			
			
			
			
		}
		
	}

}
