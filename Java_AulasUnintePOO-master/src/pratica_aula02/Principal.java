package pratica_aula02;

public class Principal {

	public static void main(String[] args) {
		
		// Manualmente:
		
		Avaliacao a = new Avaliacao(" Rafael Gouveia ", 6.5,4.5,7);
		
		
		
		System.out.println("M�dias do Aluno: " + a.nome);
		System.out.printf("M�dia Aritm�tica -  " + a.MediaAritmetica() + " \n" );
		System.out.println("M�dia Ponderada - " + a.MediaPonderada());
		System.out.println("M�dia Geral =  " + a.MediaGeral());
		System.out.println();
		
		// Semi - Manualmente:
		
		Avaliacao b = new Avaliacao(" Pollyanna Maia ", 7, 8.7, 5);
		b.info();
		
		
		Avaliacao c = new Avaliacao();
		c.info();
		
	}

}
