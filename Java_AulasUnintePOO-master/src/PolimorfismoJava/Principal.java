package PolimorfismoJava;

public class Principal {

	public static void main(String[] args) {
		
		Funcionario colaboradores [] = {
				
				new Assalariado ("Rafael", 4899),
				new Horista ("Pollyanna", 100, 40.5f),
				new Comissionado ("Giovana", 5000, 0.05f)
								
		};
		
		//variável F criada.
		Funcionario f;
		float total =0;
		
		for (int i=0; i<colaboradores.length; i++) {
			
			f = colaboradores[i];
			
			System.out.println(f.nome + " salario R$ " + f.pagamento());
			
			total += f.pagamento(); // soma de toda a olha de pagamento
			
			/*
			 * f.varivael, pega o que o aço for varreu, após a criação de F. e mostra o nome (f.nome), e o pagamento (f.pagamento())
			 */
			
			/*
			 * Em apenas um loop, estamos referenciando, através do polimorfismo, várias informações dos objetos de várias classes.
			 * Sem o polimorfismo, seria um loop para cada classe de pagmento (Horista, Assalariado, Comissionado).
			 */
		}
		
		System.out.println();
		System.out.println("Total da folha R$ " + total);

	}

}
