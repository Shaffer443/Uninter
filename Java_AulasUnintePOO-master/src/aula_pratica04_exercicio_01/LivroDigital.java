package aula_pratica04_exercicio_01;

//extends Livro, informa que a class LivroDigital � uma subclasse de Livro.

public class LivroDigital extends Livro {
	
	private int download;
	private double tamanho;
	
	
	public int getDownload() {
		return download;
	}
	public void setDownload(int download) {
		this.download = download;
	}
	public double getTamanho() {
		return tamanho;
	}
	public void setTamanho(double tamanho) {
		this.tamanho = tamanho;
	}
	
	// Construtores:
	
	public LivroDigital() {};
	
	//OBS: se precisar� adiconar os atributos da classe m�e ou se o super() j� supre.  
	public LivroDigital(String titulo, Autor autor, String genero, int edicao, int download, double tamanho) {
		super(titulo, autor, genero, edicao);
		this.download = download;
		this.tamanho = tamanho;
	}
	
	@Override //informa ao compilador que h� um subescri��o ao sistema.
	public void info() {
		
		super.info(); // super faz refer�ncia a classe m�e.
		System.out.println("Download: " + download);
		System.out.println("Tamanho do arquivo: " + tamanho);
		
		
	}
	
	
	
	
	

}
