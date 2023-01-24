import java.util.ArrayList;

public class Kontroll {
	//Vi trenger en arraylist for hver type objekt:
	private ArrayList<Person> personer = new ArrayList<>();
	private ArrayList<Postadresse> postadresser = new ArrayList<>();
	private ArrayList<Kjøretøy> kjøretøy = new ArrayList<>();
	
	//Metoder for � operere p� datastrukturene:
	public void nyPerson(Person person) {
		personer.add(person);
	}
	
	public void nyttKj�ret�y(Kj�ret�y k) {
		kj�ret�y.add(k);
	}
	
	public void nyPostadresse(int postnr, String poststed) {
		postadresser.add(new Postadresse(postnr, poststed));
	}
	
	//Vi trenger ogs� s�kemetoder:
	public Person finnPerson(String navn) {
		
	}
	
	public Kj�ret�y finnKj�ret�y(String regnr) {
		
	}
	
	public Postadresse finnPostadresse(int postnr) {
		
	}
	
	//Nyttig med metoder for � returnere referanser
	//til datastrukturene:
	public ArrayList<Person> getPersoner() {
		return personer:
	}
	
	public ArrayList<Kj�ret�y> getKj�ret�y() {
		return kj�ret�y;
	}
	
	
	public ArrayList<Postadresse> getPostadresser() {
		return postadresser;
	}

}
