package herancajava;

public class Livro {

	public String autor;
	public float custoproducao;
	public float precovenda;
	public String titulo;
	public int paginas;
	
	// Construtor:
	
	public Livro(String titulo, String autor) {
		//construtor invocado em Livro Digital.
		// para refer�nciar esses par�emtros para as vari�veis criadas usamos o this.
		
		this.titulo = titulo;
		this.autor=autor;
	}
	
	//fun��o(m�todos):
	
	public float lucro() {
		
		return precovenda - custoproducao;
		
	}
	
	public void imprimirTitulo() {
		
		System.out.println("O titulo: " + titulo);
		
	}
	
	public float imposto() {
		
		return 0.2f*lucro();
		
	}
	
}
