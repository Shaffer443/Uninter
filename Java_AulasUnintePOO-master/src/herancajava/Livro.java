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
		// para referênciar esses parâemtros para as variáveis criadas usamos o this.
		
		this.titulo = titulo;
		this.autor=autor;
	}
	
	//função(métodos):
	
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
