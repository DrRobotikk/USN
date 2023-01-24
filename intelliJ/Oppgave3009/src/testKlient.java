public class testKlient {
    //En testKlient skal teste ut alle valgene
    //som skal kunne foretas i et fremtidig grensesnitt

    public static void main(String[] args) {

        OppgaveOversikt oversikt = new OppgaveOversikt();
        //Oppretter to studenter:
        Student student = new Student("Lise",2);
        boolean ok = oversikt.nyStudent(student);
        if(!ok) System.out.println("Ikke plass til flere studenter");

        student = new Student("Ole", 0);
        oversikt.nyStudent(student);
        //Sorterer:
        oversikt.sorter();
        //Søker:
        Student stud = oversikt.finnStudent("Ole");
        if (stud != null) System.out.println(stud.toString());
        else System.out.println("Fant ikke studenten");
        //Søke på en vi vet ikke finnes:
        stud = oversikt.finnStudent("Petter");
        if (stud != null) System.out.println(stud.toString());
        else System.out.println("Fant ikke studenten");



    }
}
