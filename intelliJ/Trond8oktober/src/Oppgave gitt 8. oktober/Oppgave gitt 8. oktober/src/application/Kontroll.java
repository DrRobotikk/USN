import java.util.ArrayList;
import java.util.Collections;

public class Kontroll {
	private ArrayList<Person> personer = new ArrayList<>();
	private ArrayList<Postadresse> postadresser = new ArrayList<>();
	private ArrayList<Kjøretøy> kjøretøyene = new ArrayList<>();
	
	public void nyPerson(String navn, String adresse, String postnr) {
		Postadresse postadresse = finnPostadresse(postnr);
		personer.add(new Person(navn, adresse, postadresse));
	}
	
	public void nyPostadresse(String pnr, String poststed) {

		postadresser.add(new Postadresse(pnr, poststed));
	}
	
	public void nyttKjøretøy(Kjøretøy kjøretøy) {
		kjøretøyene.add(kjøretøy);
	}
	
	public Postadresse finnPostadresse(String pnr){
		Collections.sort(postadresser);
		for(int i = 0;i < postadresser.size();i++) {
			Postadresse padr = postadresser.get(i);
			if(padr.getPostnr().equals(pnr)) return padr;
		}
		return null;		
	}
	
	public Person finnPerson(String navn) {
		for(int i = 0; i < personer.size(); i++) {
			Person p = personer.get(i);
			String pnavn = p.getNavn();
			if(pnavn.contentEquals(navn)) return p;
		}
		return null;
	}
	
	public Kjøretøy finnKjøretøyBinært(String regnr) {
		//Får vi kan bruke binærsøk må datastrukturen sorteres.
		//Dette krever igjen at klassen Kjøretøy implementerer Comparable:
		Collections.sort(kjøretøyene);
		//Siden bin�rs�k sammenligner to og to objekter,
		//lager vi et Kj�ret�y-objekt som inneholder registreringsnummeret vi søker:
		Kjøretøy dummy = new Kjøretøy(regnr, null, null);
		//Binærsøk-metoden returnerer indeksen til det objektet som har det
		//søkte registreringsnummeret. Hvis den ikke finner noe, returneres
		//et negativt tall:
		int indeks = Collections.binarySearch(kjøretøyene, dummy);
		//Vi tester så på om noe ble funnet:
		if(indeks >=0) return kjøretøyene.get(indeks);
		else return null;
	}
	
	public ArrayList<Person> getPersoner() {
		return personer;
	}
	
	public ArrayList<Kjøretøy> getKjøretøy() {
		return kjøretøyene;
	}


}
