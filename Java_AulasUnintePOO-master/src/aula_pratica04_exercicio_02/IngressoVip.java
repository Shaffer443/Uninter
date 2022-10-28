package aula_pratica04_exercicio_02;

public class IngressoVip extends Ingresso {
	
		public double adicional;
		
		
		
		public IngressoVip(String nomedoevento, double valor, double adicional) {
			super(nomedoevento, valor);
			this.adicional = adicional;
		}
		
		
	
		@Override
		public void imprimir() {
			super.imprimir();
			System.out.println("Valor Adicional R$ " + adicional);
			System.out.println("Valor Total R$ " + (valor + adicional));
			
			
		}



		


		

}
