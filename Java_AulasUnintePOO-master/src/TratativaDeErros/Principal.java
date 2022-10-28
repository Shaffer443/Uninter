package TratativaDeErros;

public class Principal {

	public static void main(String[] args) {
		
		int numeros []= {1,2,3};
		
		// C�dificando com o erro. Chamando uma posi��o que n�o existe na lista.
		
		//System.out.println(numero[8]);
		
		//try + ctrl+espa�o - atalho para a composi��o.
		try {
			
			System.out.println(numeros[8]); // c�piando o erro, acusado pel sistema JVM.
			
		} catch (Exception e) { // pode-se fazer mais de um catch.
			
			System.out.println("Ocorreu um Erro. Est� Chamando uma posi��o inexistente na lista."); //mensagem configurada por mim ao usu�rio.
			System.out.println(e.getMessage()); //chamando o erro pelo throwable (padr�o de erro do JVM
			
		}
		
		finally {
			System.out.println();
			System.out.println("O finally sempre � executado, independentemente se acontece erros ou n�o, estando dentro do c�digo.");
			
		}
	}

}
