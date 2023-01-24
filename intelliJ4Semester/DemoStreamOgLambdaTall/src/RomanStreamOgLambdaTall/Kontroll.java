package RomanStreamOgLambdaTall;

import java.util.LinkedList;

public class Kontroll {
    TestKlient testKlient = new TestKlient();

    public LinkedList deleListe = new LinkedList();
    Filtrering divisjon = (a, b) -> a%b==0;


    public void liste(int makstall) {
        for (int i=1; i<=makstall; i++) {
            deleListe.add(i);
        }
    }

    public void lambda(int deletall) {
        for (int j=0; j<deleListe.size(); j++) {
            if (divisjon.filtrer((int)deleListe.get(j),deletall)) {
                System.out.println(deleListe.get(j));
            }
        }
    }

    public void stream(int deletall) {
        deleListe.stream().filter(x -> divisjon.filtrer((int)x,deletall)).forEach(x -> System.out.println(x));
    }
}
