package EnumJava;

public class Principal {

	public static void main(String[] args) {
		
		/*
		 * Presimamo declara o ENUM e o seu TOPICO, neste exemplo. DE acordo com o construtor solicitar.
		 * Sempre mencionando o nome da classe ENUM . o TOPICO alvo instanciado no objeto.
		 */
		
		Mensagem m1 = new Mensagem(Frase.Fe);
		m1.texto();
	}

}
