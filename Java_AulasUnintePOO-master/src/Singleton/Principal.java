package Singleton;

public class Principal {

	public static void main(String[] args) {
		
		Singleton s1 = Singleton.getInstance();
		Singleton s2 = Singleton.getInstance();
		
		//incrementadno o s1 em 10:
		
		s1.numero+=10;
		System.out.println(s1.numero);
		System.out.println(s2.numero);
		
		/*
		 * Se alterar tanto no s1 qaunto no s2, significa que estamos trabalhando com a mesma  instancia.
		 */
		
		// Espramos que em ambos de 30 do primeiro teste + 40 do segundo. Resposta 80.
		
		
		s2.numero+=50;
		System.out.println(s1.numero);
		System.out.println(s2.numero);
		
		
		/*
		 * Signifcia que quantas ves eu alteras, uma mudançad e um vale para todas as instância Singleton.
		 * 
		 * Quase uma variável global. Só que aqui é para dentro do projeto inteiro.
		 */
	}

}
