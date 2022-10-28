package aula03_localdate;

import java.time.LocalDate;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;


public class Principal {

	public static void main(String[] args) {
		// Classe que representa Data.
		
		//informa a data de hoje:
		
		LocalDate datahoje = LocalDate.now();
		
		System.out.println("Data em formatado padr�o:");
		System.out.println(datahoje);
		
		// Fun��o que organiza o formato da data:
		
		DateTimeFormatter formatador = DateTimeFormatter.ofPattern("dd/MM/yyyy");
		
		System.out.println("Data depois dos par�metros de formata��o:");
		System.out.println(datahoje.format(formatador));
		
		// Fun��o que organiza o formato da data e adiocionando o dia da semana,adicionando E mai�sculo:
		
			DateTimeFormatter formatador_dia = DateTimeFormatter.ofPattern("dd/MM/yyyy - E");
		
			System.out.println("Data depois dos par�metros de formata��o + Dia da semana:");
			System.out.println(datahoje.format(formatador_dia));
			
			// adicionando mais EEEE, ele representa por extenso:
			
				DateTimeFormatter formatador_diacompleto = DateTimeFormatter.ofPattern("dd/MM/yyyy - EEEE");
				
				System.out.println("Data depois dos par�metros de formata��o + Dia da semana completo:");
				System.out.println(datahoje.format(formatador_diacompleto));
		
		
	// Trabalhando com horas (tempo):
				
	LocalTime hora = LocalTime.now();
	
	System.out.println("Hora atual padr�o:");
	System.out.println(hora);
	
	
	// Fun��o que organiza o formato da hora:
	
			DateTimeFormatter formatadortime = DateTimeFormatter.ofPattern("HH:mm:ss");
			
			System.out.println("Data depois dos par�metros de formata��o:");
			System.out.println(hora.format(formatadortime));
				
			
			// Fun��o que organiza o formato da data e adiocionando o dia da semana,adicionando E mai�sculo:
			// adicionando mais EEEE, ele representa por extenso:
			// pegando dados da variavel datahoje:
			
				DateTimeFormatter formatadortimedia = DateTimeFormatter.ofPattern("HH:mm:ss - EEEE");
				DateTimeFormatter diacompleto = DateTimeFormatter.ofPattern(" EEEE");
			
				System.out.println("Data depois dos par�metros de formata��o:");
				System.out.println(hora.format(formatadortime) + diacompleto.format(datahoje) );
				
				
				
				
	// Class que engloba os dados: horario atual, data e dia:
				
				hoje informacao = new hoje();
				
				informacao.info();
				
	}

}
