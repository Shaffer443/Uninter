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
		 * Com a Interface, não podemos instânciar. porem podemos atribuir uma váriável, e através desta variável puxar o método 
		 * inserido na classe da interface.
		 * 
		 * No caso, só temos umac lasse interface, porém, se tivesse outras, pdoeriamso tamber adiciona-las as classes.
		 * 
		 *  exemplo: public class Familia implements Imprimivel, SegundaINterface(){}
		 *  
		 *  Essa é agrande diferença. Na herança, só podemos herdar uma classe abstrata, por exemplo.
		 *  Na interface, podemos herdar várias classes de interface.
		 */
		
		
	}

}
