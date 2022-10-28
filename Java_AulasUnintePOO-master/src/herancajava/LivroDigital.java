package herancajava;

/*
 * extends + classe " a se clonar", evitamos reescrever novamente códigos e "cópia" uma classe alvo e seus atributos.
 * No caso, estamos copiando a classe Livros.
 * 
 * Com isso, basta adicionar o que é necessário ou exclusivo para esta nova classe, sem precisar reescrever códigos.
 * 
 * Toda alteração no código, atributos ou métodos em Livro, já é atualizada automaticamente para Livro Digital.
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
	
	// Diferença:
	
	public float imposto() {
		
		return 0.2f*lucro() + 2 ;
		
	}
	
	// Novo:
	
	public float tamanhoporpagina() {
		
		return tamanhomb/(float)paginas;
		
	}
	
	//Exemplo de como se puxar dar de m[étodos de uma classe mãe
	
	public void infoImposto(){
		
		System.out.println("Imposto livro Físico: " + super.imposto()); // puxando da clss mãe "Livro"
		System.out.println("Imposto livro Digital: " + imposto()); // Puxando desta classe Livro Digital
		
	}

}
