package aula05_exercicio02;

import java.util.ArrayList;

public class Principal {

	public static void main(String[] args) {
		
		Familia pessoa1 = new Familia("Rafael", "Gouveia");
		Relacao pessoa2 = new Relacao("Pai | Namorado | Filho");
		Ocupacao pessoa3 = new Ocupacao("Estudante");
		
		pessoa1.imprimir();
		pessoa2.imprimir();
		pessoa3.imprimir();
		
		ArrayList <Imprimivel> ListaFamilia = new ArrayList();
		
		
		ListaFamilia.add(new Familia("Pollyanna","Maia"));
		ListaFamilia.add(new Relacao("Namorada | Filha"));
		ListaFamilia.add(new Ocupacao("Designer | Estudante"));
		 System.out.println();
		
		for(Imprimivel lista : ListaFamilia) {
			 
			 lista.imprimir();

		}
		
		
		
		System.out.println();
		
		Imprimivel mostrar = pessoa1;
		mostrar.imprimir();
		
		mostrar = pessoa2;
		mostrar.imprimir();
		
		mostrar = pessoa3;
		mostrar.imprimir();
		
		
		/*
		 * Com a Interface, n�o podemos inst�nciar. porem podemos atribuir uma v�ri�vel, e atrav�s desta vari�vel puxar o m�todo 
		 * inserido na classe da interface.
		 * 
		 * No caso, s� temos umac lasse interface, por�m, se tivesse outras, pdoeriamso tamber adiciona-las as classes.
		 * 
		 *  exemplo: public class Familia implements Imprimivel, SegundaINterface(){}
		 *  
		 *  Essa � agrande diferen�a. Na heran�a, s� podemos herdar uma classe abstrata, por exemplo.
		 *  Na interface, podemos herdar v�rias classes de interface.
		 */
		
		
	}

}
