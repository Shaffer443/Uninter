package aula03_localdate;

import java.time.LocalDate;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;

public class hoje {
	
	void info() {
	LocalTime hora = LocalTime.now();
	LocalDate datahoje = LocalDate.now();
	
	DateTimeFormatter formatadortime = DateTimeFormatter.ofPattern("HH:mm:ss");
	DateTimeFormatter formatador_diacompleto = DateTimeFormatter.ofPattern("dd/MM/yyyy - EEEE");

	System.out.println("# Horário - Data - Dia | Atualizado #");
	System.out.println("Hora: " + hora.format(formatadortime) + " | " + " Data: " + datahoje.format(formatador_diacompleto));
	
	}

}
