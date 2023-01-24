//Oppretter class'en 'Person'
public class ToPersoner{
    //Oppretter attributtene navn og adresse:
    String navn;

    //Konstruktør:
    public Person(String navn){
        this.navn=navn;//Attributtet 'navn' settes til parameter
    }
    public String toString() {
        return "**********\n" + "navn: " + navn + "\n**********";}
}

