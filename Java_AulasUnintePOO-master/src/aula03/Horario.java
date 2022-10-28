package aula03;

/* Organizar Modelo de informa��o de hor�rio, com set e get.
 * get = pegar
 * set = definir
 * 
 * premissa de n�o permitir hor�rios fora do pradr�o. 
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
	
	// Definindo um par�metro de seguran�a para uma faixa permitida de hora (0 a 23)
	
	public void setHora(int hora) {
		
		if(hora >= 0 && hora<=23) {
			
			this.hora=hora;
		}else {
			
			System.out.println("Hor�rio Inv�lido");
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
			
			System.out.println("Minuto(os) inv�lido");
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
			
			System.out.println(" Segundos inv�lido ");
		}
		
	}
	
	// Retorno de Informa��es:
	
	void info() {
		
		System.out.println("Hor�rio");
		System.out.println(""+ hora +":" + minuto + ":" + segundo);
		
	}

}
