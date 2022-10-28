package aula_pratica04_exercicio_01;

public class Autor {
	
	private String nome;
	private String email;
	private String nacionalidade;
	
	
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	public String getNacionalidade() {
		return nacionalidade;
	}
	public void setNacionalidade(String nacionalidade) {
		this.nacionalidade = nacionalidade;
	}
	
	//1 - Construtor vazio:
	
	public Autor() {}
	
	//2 - Construtor com parâmetros:
	
	public Autor(String nome, String email, String nacionalidade) {
		super();
		this.nome = nome;
		this.email = email;
		this.nacionalidade = nacionalidade;
	}
	
	void info() {
		
		System.out.println("Nome do Autor(a): " + nome);
		System.out.println("E-mail do Autor(a): " + email);
		System.out.println("Nacionalidade do Autor(a): " + nacionalidade);
		
		
		
	}
	
	
	
	
	

}
