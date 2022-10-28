package aula_pratica04_exercicio_01;


	// extends Livro, informa que a class LivroFisico é uma subclasse de Livro.
	public class LivroFisico extends Livro {
	
	private int tiragem;
	private int peso;
	
	
	public int getTiragem() {
		return tiragem;
	}
	public void setTiragem(int tiragem) {
		this.tiragem = tiragem;
	}
	public int getPeso() {
		return peso;
	}
	public void setPeso(int peso) {
		this.peso = peso;
	}
	
	//Construtores:
	
	public LivroFisico() {} //Só pode ser criado pq na classe mãe tb existe um cosntrutor vázio. Caso contrario daria erro.
	//OBS: se precisará adiconar os atributos da classe mãe ou se o super() já supre.  
	public LivroFisico( String titulo, Autor autor, String genero, int edicao, int tiragem, int peso) {
		super(titulo, autor, genero, edicao);
		this.tiragem = tiragem;
		this.peso = peso;
	}
	
	@Override //informa ao compilador que há um subescrição ao sistema.
	public void info() {
		
		super.info(); // super faz referência a classe mãe.
		System.out.println("Nº da tiragem: " + tiragem);
		System.out.println("Peso: " + peso + " g");
		
	}

	

	

}
