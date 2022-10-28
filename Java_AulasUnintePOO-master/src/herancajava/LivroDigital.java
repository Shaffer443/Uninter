package herancajava;

/*
 * extends + classe " a se clonar", evitamos reescrever novamente c�digos e "c�pia" uma classe alvo e seus atributos.
 * No caso, estamos copiando a classe Livros.
 * 
 * Com isso, basta adicionar o que � necess�rio ou exclusivo para esta nova classe, sem precisar reescrever c�digos.
 * 
 * Toda altera��o no c�digo, atributos ou m�todos em Livro, j� � atualizada automaticamente para Livro Digital.
 * 
 */

public class LivroDigital extends Livro {
	
	public String linkdownload;
	public int tamanhomb;
	
	public LivroDigital(String titulo, String autor, String linkdownload) {
		// Super tem que ser, obrigatoriamente o primeiro da classe clone.
		super(titulo, autor);
		this.linkdownload = linkdownload;
	}
	
	// Diferen�a:
	
	public float imposto() {
		
		return 0.2f*lucro() + 2 ;
		
	}
	
	// Novo:
	
	public float tamanhoporpagina() {
		
		return tamanhomb/(float)paginas;
		
	}
	
	//Exemplo de como se puxar dar de m[�todos de uma classe m�e
	
	public void infoImposto(){
		
		System.out.println("Imposto livro F�sico: " + super.imposto()); // puxando da clss m�e "Livro"
		System.out.println("Imposto livro Digital: " + imposto()); // Puxando desta classe Livro Digital
		
	}

}
