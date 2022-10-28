package herancajava;

/* 
 * Usada de Exemplo, de como normalmente se faria, não usando a herença.
 */

public class LivroDigitalEx {
	
	public String autor;
	public float custoproducao;
	public float precovenda;
	public String titulo;
	public int paginas;
	
	
	public String linkdownload;
	public int tamanhomb;
	
	//função(métodos):
	
	public float lucro() {
		
		return precovenda - custoproducao;
		
	}
	
	public void imprimirTitulo() {
		
		System.out.println("O titulo: " + titulo);
		
	}
	
	// Diferença:
	
	public float imposto() {
		
		return 0.2f*lucro() + 2 ;
		
	}
	
	// Novo:
	
	public float tamanhoporpagina() {
		
		return tamanhomb/(float)paginas;
		
	}
	
	

}
