package trond.Oblig1_2019;

public class Dikter {
	//Definerer en konstant ANTALL gir den totale
	//lengden p� alle arrayene:
	private final int ANTALL = 20;
	//Definerer og oppretter array'en som skal brukes 
	//for � lage enkle dikt. Her skilles ikke mellom
	//ordklasser:
	private String[] ordliste = new String[ANTALL];
	//I stedet for � bruke en teller for � holde
	//rede p� antall ord som settes inn i array'en
	//definerer jeg rett og slett antallet her. Da
	//m� jeg la konstrukt�ren for Dikter opprette dette
	//antallet ord:
	private int antallord = 15;
	//Det samme gjelder for de fire array'ene for de fire 
	//ordklassene.
	private String[] verbliste = new String[ANTALL];
	private int antallverb = 6;
	private String[] subliste = new String[ANTALL];
	private int antallsub = 7;
	private String[] adjliste = new String[ANTALL];
	private int antalladj = 6;
	private String[] advliste = new String[ANTALL];
	private int  antalladv = 6;
	
	//Jeg lar konstrukt�ren opprette en rekke ord
	//b�de for den enkle og den avanserte diktgeneratoren:
	public Dikter() {
		ordliste[0] = "kan";
		ordliste[1] = "sover";
		ordliste[2] = "bilen";
		ordliste[3] = "huset";
		ordliste[4] = "spiser";
		ordliste[5] = "lille";
		ordliste[6] = "store";
		ordliste[7] = "ut";
		ordliste[8] = "inn";
		ordliste[9] = "øst";
		ordliste[10] = "vest";
		ordliste[11] = "løper";
		ordliste[12] = "gode";
		ordliste[13] = "den";
		ordliste[14] = "det";
		verbliste[0] = "går";
		verbliste[1] = "sover";
		verbliste[2] = "kryper";
		verbliste[3] = "leser";
		verbliste[4] = "spiser";
		verbliste[5] = "kjører";
		subliste[0] = "huset";
		subliste[1] = "bilen";
		subliste[2] = "studenten";
		subliste[3] = "hunden";
		subliste[4] = "skolen";
		subliste[5] = "osten";
		subliste[6] = "ølet";
		adjliste[0] = "grønne";
		adjliste[1] = "trette";
		adjliste[2] = "store";
		adjliste[3] = "sterke";
		adjliste[4] = "lille";
		adjliste[5] = "våte";
		advliste[0] = "pene";
		advliste[1] = "vonde";
		advliste[2] = "stygge";
		advliste[3] = "slitne";
		advliste[4] = "dovne";
		advliste[5] = "svære";
	}
	
	//Metoden regOrd() er den som legger ord
	//inn i array'en for den enkle diktgeneratoren:
	public void regOrd(String ord) {
		if(antallord < ordliste.length) {
			ordliste[antallord] = ord;
			antallord++;
		}		
	}
	
	//Disse fire metodene legger hver sin type ord inn
	//i riktig array. Disse brukes til � lage avanserte dikt:
	public boolean regVerb(String verb) {
		//Siden vi bruker en array, m� vi teste p� om
		//det er plass i array'en:
		if(antallverb < verbliste.length) {
			verbliste[antallverb] = verb;
			antallverb++;
			return true; //Det var plass
		}	
		else return false; //Det var ikke plass
	}
	
	public boolean regSub(String sub) {
		if(antallsub < subliste.length) {
			subliste[antallsub] = sub;
			antallsub++;
			return true;
		}
		else return false;
	}
	
	public boolean regAdj(String adj) {
		if(antalladj < adjliste.length) {
			adjliste[antalladj] = adj;
			antallord++;
			return true;
		}
		else return false;
	}
	
	public boolean regAdv(String adv) {
		if(antalladv < advliste.length) {
			advliste[antalladv] = adv;
			antalladv++;
			return true;
		}
		else return false;
	}
	
	//Metode for � lage et enkelt dikt:
	public String lagDikt() {
		//Lager en tom String for diktet:
		String dikt = "";
		//Den ytre l�kken teller linjer:
		for(int i = 0;i < 4;i++) {
			//Den indre l�kken teller ord p� hver linje:
			for(int j = 0;j < 4;j++) {
				//Kaller lagTilfeldig() for � f� et
				//tilfeldig tall innenfor antallet ord i array'en:
				int tilfeldig = lagTilfeldig(antallord);
				String ord = ordliste[tilfeldig];
				dikt+=ord+" ";
			}	//indre for
			//Legger til linjeskift:
		dikt+="\n";
		} //ytre for
		//Returnerer et dikt p� 4 linjer, med 4 ord p� hver linje:
		return dikt;		
	}
	
	//Metode som genererer et tilfeldig tall mellom 0 og 1 mindre
	//enn antall elementer i en array:
	public int lagTilfeldig(int lengde) {
		int t=0;
		//Bruker metoden Math.random() for � f� et tilfeldig tall:
		t=(int)(Math.random()*(lengde - 1));
		//Returnerer tallet:
		return t;
	} //Slutt metode
	
	//Metode som lager et avansert dikt:
	public String lagAvansert() {
		String dikt = "";
		//De 3 f�rste linjene skal ha samme struktur:
		for(int i = 0;i < 3;i++) {
				int tilfeldig = lagTilfeldig(antalladv);
				String ord = advliste[tilfeldig];
				dikt+=ord+" ";
				tilfeldig = lagTilfeldig(antallsub);
				ord = subliste[tilfeldig];
				dikt+=ord+" ";
				tilfeldig = lagTilfeldig(antallverb);
				ord = verbliste[tilfeldig];
				dikt+=ord+" ";
				tilfeldig = lagTilfeldig(antalladj);
				ord = adjliste[tilfeldig];
				dikt+=ord+" ";
				dikt+="\n";
			}	//indre for
			//Siste linje skal ha en annen struktur:
			int tilfeldig = lagTilfeldig(antallverb);
			String ord = verbliste[tilfeldig];
			dikt+=ord+" ";
			tilfeldig = lagTilfeldig(antalladj);
			ord = adjliste[tilfeldig];
			dikt+=ord+" ";
			tilfeldig = lagTilfeldig(antalladv);
			ord = advliste[tilfeldig];
			dikt+=ord+" ";
			tilfeldig = lagTilfeldig(antallsub);
			ord = subliste[tilfeldig];
			dikt+=ord+" ";
			dikt+="\n";
			dikt+="\n";
		
			//Returnerer diktet		
			return dikt;
	}

}
