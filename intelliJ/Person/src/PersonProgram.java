public class PersonProgram {
    //Dette er selve programmet

    public static void main(String[] args) {
        //Oppretter personobjekter:
        Person p1 = new Person("Ole","Klekkenveien 1");
        Person p2 = new Person("Lise","Enannenvei 3");
        //Skriver ut navn og adresse til objektene p1 og p2
        System.out.println(p1.toString());
        System.out.println(p2.toString());
    }
}
