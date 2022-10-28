package aula_pratica04_exercicio_01;


	// extends Livro, informa que a class LivroFisico � uma subclasse de Livro.
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
	
	public LivroFisico() {} //S� pode ser criado pq na classe m�e tb existe um cosntrutor v�zio. Caso contrario daria erro.
	//OBS: se precisar� adiconar os atributos da classe m�e ou se o super() j� supre.  
	public LivroFisico( String titulo, Autor autor, String genero, int edicao, int tiragem, int peso) {
		super(titulo, autor, genero, edicao);
		this.tiragem = tiragem;
		this.peso = peso;
	}
	
	@Override //informa ao compilador que h� um subescri��o ao sistema.
	public void info() {
		
		super.info(); // super faz refer�ncia a classe m�e.
		System.out.println("N� da tiragem: " + tiragem);
		System.out.println("Peso: " + peso + " g");
		
	}

	

	

}
