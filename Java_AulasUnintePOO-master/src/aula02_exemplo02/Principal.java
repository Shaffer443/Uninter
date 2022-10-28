package aula02_exemplo02;

public class Principal {

	public static void main(String[] args) {
		
		/* Carro - Chamando uma classe para usar na classe Principal.
		 * Como se chamasse uma função.
		 * new Carro() - instanciando um novo objeto, Carro a. 
		 */
		
		Carro a = new Carro();

		/* Chamamos a classe, passamos a função e o parâmetro para tranformação.
		 * Virando um método da class, enão do objeto.
		 */
		
		System.out.println(Carro.MilharParaMetros(10));
		
		// Passa-se o parâmetro dentro de (x).
		
		// Tentando alterar o valor de PI travado pelo FINAL.
		
		// Carro.PI=4.00; o Sistema não permite a alteração de valor.
		
		// Usando o Sistema:
		
		a.info(); // cahmando antes de alterar
		
		System.out.println();
		
		a.nome = "Etios";
		a.modelo = "Etios";
		a.autonomia = 200;
		
		a.info(); // chamando depois de alterar
		
		
	}

}
