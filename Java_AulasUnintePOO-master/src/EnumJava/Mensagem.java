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
			
			System.out.println(" Que nunca nos falte esperança de dias melhores");
			break;
			
		case Paz:
			
			System.out.println("A paz de espírito é quando o seu coração está em sintonia com a sua mente.");
			break;
			
		case Fe:
			
			System.out.println("Não foi a fé que conquistou meus feitos, mas sem ela não os teria alcançado!");
			break;
			
		default:
			System.out.println("Erro. Tema inextente. Tente outro.");
		}
		
		
	}
}
