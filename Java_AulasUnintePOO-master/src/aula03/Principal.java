package aula03;

public class Principal {

	public static void main(String[] args) {
		
		Horario aula = new Horario();
		
		// Lembrar que após o métido, o atributo é maiúsculo (setHora,setMinuto,setSegundo)
		
		/* Usado o setting na Hora,Minuto e Segundos. Passando os parâmetros permitdos.
		 * Com isso, o sistema já acusa erro, caso esteja fora dos parâmetro.
		 */
		
		
		aula.setHora(12);
		aula.setMinuto(54);
		aula.setSegundo(10);
		
		aula.info();

		
	}

}
