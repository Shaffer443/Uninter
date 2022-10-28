package aula_pratica04_exercicio_01;

public class Livro {
	//Usando prtected no ligar de private, o protected dá acesso as classes filhos, unsando extends.(ex: extends Livro)

	protected String titulo;
	protected Autor autor;
	protected String genero;
	protected int edicao;
	
	
	public String getTitulo() {
		return titulo;
	}
	public void setTitulo(String titulo) {
		this.titulo = titulo;
	}
	public Autor getAutor() {
		return autor;
	}
	public void setAutor(Autor autor) {
		this.autor = autor;
	}
	public String getGenero() {
		return genero;
	}
	public void setGenero(String genero) {
		this.genero = genero;
	}
	public int getEdicao() {
		return edicao;
	}
	public void setEdicao(int edicao) {
		this.edicao = edicao;
	}
	
	//Construtor(es):
	
	public Livro() {}
	
	public Livro(String titulo, Autor autor, String genero, int edicao) {
		super();
		this.titulo = titulo;
		this.autor = autor;
		this.genero = genero;
		this.edicao = edicao;
	}
	
	
	void info() {
		
		System.out.println("Titulo: " + titulo);
		System.out.println("Nome do Autor(a): " + autor.getNome());
		System.out.println("Gênero do Livro: " + genero);
		System.out.println("Edição: " + edicao);
		
		autor.info(); //Puxando a INFO da classe Autor.
		
		
		
	}
	
	
	
	
	
	
	
}
