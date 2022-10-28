package aula03_pratica2;

	/* Crie uma classe Aluno com os:
	 * 
	 * Atributos:
	 * 
	 * string nome
	 * int matricula
	 * double desconto
	 * curso curso;
	 * 
	 * métodos:
	 * 
	 * descrever();
	 * pagamento() - Informa o preço que o aluno paga, considerando seu desconto
	 * e o preço de seu curso.
	 */

public class Aluno {
	
	 String nome;
	 int matricula;
	 double desconto;
	 Curso curso;
	 double pagamento;
	 
	 
	 Aluno(String nome, int matricula, double desconto, Curso curso){
		 
		 this.nome = nome;
		 this.matricula = matricula;
		 this.desconto = desconto;
		 this.curso = curso;
		 
	 }
	 
	 
	 
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	public int getMatricula() {
		return matricula;
	}
	public void setMatricula(int matricula) {
		this.matricula = matricula;
	}
	public double getDesconto() {
		return desconto;
	}
	public void setDesconto(double desconto) {
		this.desconto = desconto;
	}
	public Curso getCurso() {
		return curso;
	}
	public void setCurso(Curso curso) {
		this.curso = curso;
	}
	
	
	
	
	 
	double pagamento(){
			 
			return curso.mensalidade - desconto;	
		
		 }
		
	
	void info() {
		
		curso.info();
		System.out.println("Aluno: " + nome);
		System.out.println("Matricula: " + matricula);
		System.out.println("Desconto R$ " + desconto);
		System.out.println("Mensalidade Final R$ " + pagamento());
		
	}

	
	
	
	 
	 
}
