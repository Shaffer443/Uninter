package Igualdade_ToString;

import java.util.Objects;

public class Usuario {
	
	int id;
	String nome;
	String cpf;
	
	public Usuario(int id, String nome, String cpf) {
		super();
		this.id = id;
		this.nome = nome;
		this.cpf = cpf;
	}
	
	// Criação do To String:
	
	@Override
	public String toString() {
		return "Usuario [id=" + id + ", nome=" + nome + ", cpf=" + cpf + "]";
	}
	
	/*
	 * Ajuda a imprimir de forma mais simples e rápida, ao invés de solicitar concatençao de várias informações
	 */
	

	//Verificando integridade dos dados. Em rela~çao a duplicidade, local de alocação na memória e criação de um HashCode
	
	@Override
	public int hashCode() {
		return Objects.hash(cpf, id, nome);
	}

	

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Usuario other = (Usuario) obj;
		return Objects.equals(cpf, other.cpf) && id == other.id && Objects.equals(nome, other.nome);
	}
	
	
	

}
