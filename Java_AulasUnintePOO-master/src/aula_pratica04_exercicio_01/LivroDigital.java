package aula_pratica04_exercicio_01;

//extends Livro, informa que a class LivroDigital é uma subclasse de Livro.

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
	
	//OBS: se precisará adiconar os atributos da classe mãe ou se o super() já supre.  
	public LivroDigital(String titulo, Autor autor, String genero, int edicao, int download, double tamanho) {
		super(titulo, autor, genero, edicao);
		this.download = download;
		this.tamanho = tamanho;
	}
	
	@Override //informa ao compilador que há um subescrição ao sistema.
	public void info() {
		
		super.info(); // super faz referência a classe mãe.
		System.out.println("Download: " + download);
		System.out.println("Tamanho do arquivo: " + tamanho);
		
		
	}
	
	
	
	
	

}
