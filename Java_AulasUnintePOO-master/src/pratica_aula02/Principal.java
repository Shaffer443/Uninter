package pratica_aula02;

public class Principal {

	public static void main(String[] args) {
		
		// Manualmente:
		
		Avaliacao a = new Avaliacao(" Rafael Gouveia ", 6.5,4.5,7);
		
		
		
		System.out.println("Médias do Aluno: " + a.nome);
		System.out.printf("Média Aritmética -  " + a.MediaAritmetica() + " \n" );
		System.out.println("Média Ponderada - " + a.MediaPonderada());
		System.out.println("Média Geral =  " + a.MediaGeral());
		System.out.println();
		
		// Semi - Manualmente:
		
		Avaliacao b = new Avaliacao(" Pollyanna Maia ", 7, 8.7, 5);
		b.info();
		
		
		Avaliacao c = new Avaliacao();
		c.info();
		
	}

}
