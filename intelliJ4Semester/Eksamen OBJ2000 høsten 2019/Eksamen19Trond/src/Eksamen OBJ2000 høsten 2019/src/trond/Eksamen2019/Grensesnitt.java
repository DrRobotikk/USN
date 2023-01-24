import java.util.ArrayList;
import java.util.Iterator;

import javax.swing.JOptionPane;

public class Grensesnitt {
	Kontroll kontroll = new Kontroll();
	
	//Oppgave 3a:
	public void lesNyttKurs() {
		String kurskode = JOptionPane.showInputDialog("Kurskode:");
		String kursnavn = JOptionPane.showInputDialog("Kursnavn:");
		double studiepoeng = Double.parseDouble(JOptionPane.showInputDialog("Studiepoeng:"));
		kontroll.nyttKurs(new Kurs(kurskode, kursnavn, studiepoeng));
	}
	
	//Oppgave 3b:
	public void finnPerson() {
		long personnummer = Long.parseLong(JOptionPane.showInputDialog("Skriv personnummeret:"));
		Person personen = kontroll.finnPerson(personnummer);
		if(personen !=null) System.out.println(personen.toString());
		else System.out.println("Fant ikke personen");
	}
	
	//Oppgave 3c:
	public void registrerKursP�Student() {
		String kurskode = JOptionPane.showInputDialog("Kurskode:");
		Kurs kurset = kontroll.finnKursBin�rt(kurskode);
		if(kurset !=null) {
			System.out.println("Kurset: " + kurset.toString());
			long personnummer = Long.parseLong(JOptionPane.showInputDialog("Personnummer:"));
			Student studenten = (Student)kontroll.finnPerson(personnummer);
			if(studenten !=null) kontroll.regKursP�Person(kurset, personnummer);
			else System.out.println("Fant ikke personen");
		}
		else System.out.println("Fant ikke kurset");
	}
	
	//Oppgave 3d:
	public void finnPersonMedKurs() {
		long personnummer = Long.parseLong(JOptionPane.showInputDialog("Skriv personnummeret:"));
		Student studenten = (Student)kontroll.finnPerson(personnummer);
		if(studenten != null) {
			System.out.println(studenten.toString());
			ArrayList<Kurs> kursdeltagelse = studenten.getKursdeltagelse();
			for(int i = 0; i < kursdeltagelse.size(); i++) {
				System.out.println(kursdeltagelse.get(i).toString());
			}
		}
	}
	
	//Oppgave 3e:
	/*
	public void skrivAlt() {
		ArrayList<Person> personliste = kontroll.getPersoner();
		for(int i = 0; i < personliste.size(); i++) {
			Student studenten = (Student)personliste.get(i);
			System.out.println(studenten.toString());
			ArrayList<Kurs> kursene = studenten.getKursdeltagelse();
			for(int j = 0; j < kursene.size(); j++) {
				System.out.println(kursene.get(j).toString());
			}
		}
	}
	 */

	//UTVIDELSE HJEMMELEKSE TIL 18.01.2023
	public void skrivAlt() {
		ArrayList<Person> personliste = kontroll.getPersoner();
		for(int i = 0; i < personliste.size(); i++) {
			Student studenten = (Student)personliste.get(i);
			System.out.println(studenten.toString());
		}
		ArrayList<Kurs> kursene = kontroll.returnerKurs();
		System.out.println(kursene);
	}

	//TROND SIN LØSNING:
	public void skrivPersoner() {
		Iterator<Person> oppramser = kontroll.getIterator();
		while (oppramser.hasNext()) {
			System.out.println(oppramser.next().toString());
		}
	}

}
