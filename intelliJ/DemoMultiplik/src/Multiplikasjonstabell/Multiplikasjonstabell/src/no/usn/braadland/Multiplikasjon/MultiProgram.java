package Multiplikasjonstabell.Multiplikasjonstabell.src.no.usn.braadland.Multiplikasjon;

import javax.swing.JOptionPane;

public class MultiProgram {

	public static void main(String[] args) {
		//Spør etter startverdi:
		int start = Integer.parseInt(JOptionPane.showInputDialog("Skriv startverdi:"));
		//Leser sluttverdi:
		int slutt = Integer.parseInt(JOptionPane.showInputDialog("Skriv sluttverdi:"));
		//Vi trenger to løkker:
		//En ytre løkke som går fra startverdi til sluttverdi.
		//En indre løkke som går fra 1 til 10.
		//Ytre løkke:
		for(int i = start; i < slutt+1; i++) {
			System.out.println();
			System.out.println(i + " gangen:");
			//Indre løkke:
			for(int j = 1; j < 11; j++) {
				//i-telleren fra ytre lække ganges med j-telleren fra indre løkke:
				System.out.println(i + " x " + j + " = " + i*j);
			}
		}

	}

}
