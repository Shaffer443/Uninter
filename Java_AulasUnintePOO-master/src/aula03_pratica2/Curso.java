package aula03_pratica2;

 	/* a classe do Curso com os:
	 * 
	 * Atributos:
	 * 
	 * string nome
	 * double mensalidade
	 * 
	 * métodos
	 * 
	 * descrever();
	 * 
	 */

public class Curso {

	String nome;
	double mensalidade;
	
	
	Curso ( String nome, double mensalidade){
		
		this.nome = nome;
		this.mensalidade = mensalidade;
		
	}
	
	
	
	
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	public double getMensalidade() {
		return mensalidade;
	}
	public void setMensalidade(double mensalidade) {
		this.mensalidade = mensalidade;
	}

	
	static Curso c1 = new Curso("Adminsitração", 555.56);
	
	void info() {
		
		System.out.println("Curso " + nome);
		System.out.println("Valor R$" + mensalidade);
		System.out.println();
	}
	
	
	
	
	
	
	
}
