import java.util.Arrays;

public class OppgaveOversikt {

    //Denne skal holde rede på studentene
    //Hver student holder rede på egne godkjente oppgaver

    private Student[] studenter = new Student[2];
    private int antallStudenter = 0;

    //Metode for å sette inn en ny student:
    public boolean nyStudent(Student student) {
        //Tester om det er plass til et objekt til:
        if (antallStudenter < studenter.length) {
            studenter[antallStudenter] = student;
            antallStudenter++;
            return true;
        }
        //Hvis det ikke er plass
        else {
            return false;
        }
        //Alternativt kan jeg skrive:
        //else return false;
    }

    public void sorter() {
        //Bruker hjelpeklassen Arrays:
        Arrays.sort(studenter);
    }

    //Metode for linjært søk på student:
    public Student finnStudent(String søkenavn) {
        String navn;
        for(int i = 0; i < antallStudenter; i++) {
            navn = studenter[i].getNavn();
            if(søkenavn.equals(navn)) return studenter[i];
        }
        //Ikke funnet
        return null;
    }
}
