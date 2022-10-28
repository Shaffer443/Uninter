package aula_02_exemplo01;

import java.util.ArrayList;

public class Curso {

	public static void main(String[] args) {
		
		Turma nova = new Turma(); // Criando uma nova turma. Um novo objeto Turma
		
		// incluindo atributos dentro da turma NOVA:
		// Instâncias:
		
		nova.prof = new Professor();
		nova.prof.nome = "Leonardo"; // Objeto professor dentro da turma NOVA
		
		// nome é um atributo, do atributo prof, de uma turma NOVA
		nova.alunos = new ArrayList();
		nova.alunos.add(new Aluno()); // Adicionando alunos na lista (ArraList)
		nova.alunos.get(0).nome="Zé do Peixe"; //Acesssando um nome na posição zero (0), da lista. e substituindo.
		
		
		
		
		

	}

}
