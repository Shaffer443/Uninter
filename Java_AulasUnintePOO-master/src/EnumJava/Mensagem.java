package EnumJava;

	enum Frase{
	
	Esperanca,
	Paz,
	Fe
	
	}
	


public class Mensagem {
	
	Frase topico;

	
	public Mensagem(Frase topico) {
		
		this.topico = topico;
	}

	
	
	public void texto() {
		
		switch(topico) {
		
		case Esperanca:
			
			System.out.println(" Que nunca nos falte esperan�a de dias melhores");
			break;
			
		case Paz:
			
			System.out.println("A paz de esp�rito � quando o seu cora��o est� em sintonia com a sua mente.");
			break;
			
		case Fe:
			
			System.out.println("N�o foi a f� que conquistou meus feitos, mas sem ela n�o os teria alcan�ado!");
			break;
			
		default:
			System.out.println("Erro. Tema inextente. Tente outro.");
		}
		
		
	}
}
