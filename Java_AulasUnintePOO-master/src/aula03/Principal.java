package aula03;

public class Principal {

	public static void main(String[] args) {
		
		Horario aula = new Horario();
		
		// Lembrar que ap�s o m�tido, o atributo � mai�sculo (setHora,setMinuto,setSegundo)
		
		/* Usado o setting na Hora,Minuto e Segundos. Passando os par�metros permitdos.
		 * Com isso, o sistema j� acusa erro, caso esteja fora dos par�metro.
		 */
		
		
		aula.setHora(12);
		aula.setMinuto(54);
		aula.setSegundo(10);
		
		aula.info();

		
	}

}
