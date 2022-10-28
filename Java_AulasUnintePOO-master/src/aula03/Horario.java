package aula03;

/* Organizar Modelo de informação de horário, com set e get.
 * get = pegar
 * set = definir
 * 
 * premissa de não permitir horários fora do pradrão. 
 * 
 * Exemplo:
 * 
 * 50(hora):70(minuto):120(segundo)
 */

public class Horario {
	
	private int hora; 
	private int minuto;
	private int segundo;
	
	//HORA:
	
	public int getHora() {
		
		return hora;
	}
	
	// Definindo um parâmetro de segurança para uma faixa permitida de hora (0 a 23)
	
	public void setHora(int hora) {
		
		if(hora >= 0 && hora<=23) {
			
			this.hora=hora;
		}else {
			
			System.out.println("Horário Inválido");
		}
	}
	
	//MINUTO:

	public int getMinuto() {
		return minuto;
	}

	public void setMinuto(int minuto) {
		
		if(hora >= 0 && hora<=59) {
			
			this.minuto = minuto;
			
		}else {
			
			System.out.println("Minuto(os) inválido");
		}
		
	}
	
	//SEGUNDO:

	public int getSegundo() {
		return segundo;
	}

	public void setSegundo(int segundo) {
		
		if(hora >= 0 && hora<=59) {
			
			this.segundo = segundo;
			
		}else {
			
			System.out.println(" Segundos inválido ");
		}
		
	}
	
	// Retorno de Informações:
	
	void info() {
		
		System.out.println("Horário");
		System.out.println(""+ hora +":" + minuto + ":" + segundo);
		
	}

}
