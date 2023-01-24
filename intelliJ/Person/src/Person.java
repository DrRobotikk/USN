//Oppretter class'en 'Person'
public class Person{
    //Oppretter attributtene navn og adresse:
    String navn;
    String adresse;

    //Konstruktør:
    public Person(String navn, String adresse){
        this.navn=navn;//Attributtet 'navn' settes til parameter
        this.adresse=adresse;//Attributtet 'adresse' settes til parameter
    }
    public String toString(){return navn+", "+adresse;}
}

