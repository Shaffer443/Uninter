package Igualdade_ToString;

public class Principal {

	public static void main(String[] args) {
		
		Usuario u1 = new Usuario(001, "Rafael", "222333444");
		
		System.out.println(u1); // rodando sem cria a ToString, obtem o resultad: Igualdade.Usuario@e78b58a2
		
		System.out.println(u1); //apos a criação de To String na class Usuario, aparece as informações

	}

}
