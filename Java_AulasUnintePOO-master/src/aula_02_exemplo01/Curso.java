package aula_02_exemplo01;

import java.util.ArrayList;

public class Curso {

	public static void main(String[] args) {
		
		Turma nova = new Turma(); // Criando uma nova turma. Um novo objeto Turma
		
		// incluindo atributos dentro da turma NOVA:
		// Inst�ncias:
		
		nova.prof = new Professor();
		nova.prof.nome = "Leonardo"; // Objeto professor dentro da turma NOVA
		
		// nome � um atributo, do atributo prof, de uma turma NOVA
		nova.alunos = new ArrayList();
		nova.alunos.add(new Aluno()); // Adicionando alunos na lista (ArraList)
		nova.alunos.get(0).nome="Z� do Peixe"; //Acesssando um nome na posi��o zero (0), da lista. e substituindo.
		
		
		
		
		

	}

}
