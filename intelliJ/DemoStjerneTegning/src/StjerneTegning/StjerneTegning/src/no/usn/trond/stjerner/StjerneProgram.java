package StjerneTegning.StjerneTegning.src.no.usn.trond.stjerner;

public class StjerneProgram {

	public static void main(String[] args) {
		//Lager et objekt av klassen Grensesnitt:
		Grensesnitt grensesnitt = new Grensesnitt();
		//Overlater programkontrollen til grensesnittet:
		grensesnitt.meny();
	}

}
