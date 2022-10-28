package TratativaDeErros;

public class Principal {

	public static void main(String[] args) {
		
		int numeros []= {1,2,3};
		
		// Códificando com o erro. Chamando uma posição que não existe na lista.
		
		//System.out.println(numero[8]);
		
		//try + ctrl+espaço - atalho para a composição.
		try {
			
			System.out.println(numeros[8]); // cópiando o erro, acusado pel sistema JVM.
			
		} catch (Exception e) { // pode-se fazer mais de um catch.
			
			System.out.println("Ocorreu um Erro. Está Chamando uma posição inexistente na lista."); //mensagem configurada por mim ao usuário.
			System.out.println(e.getMessage()); //chamando o erro pelo throwable (padrão de erro do JVM
			
		}
		
		finally {
			System.out.println();
			System.out.println("O finally sempre é executado, independentemente se acontece erros ou não, estando dentro do código.");
			
		}
	}

}
