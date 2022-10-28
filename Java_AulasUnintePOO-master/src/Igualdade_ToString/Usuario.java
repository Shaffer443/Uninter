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
	
	// Cria��o do To String:
	
	@Override
	public String toString() {
		return "Usuario [id=" + id + ", nome=" + nome + ", cpf=" + cpf + "]";
	}
	
	/*
	 * Ajuda a imprimir de forma mais simples e r�pida, ao inv�s de solicitar concaten�ao de v�rias informa��es
	 */
	

	//Verificando integridade dos dados. Em rela~�ao a duplicidade, local de aloca��o na mem�ria e cria��o de um HashCode
	
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
