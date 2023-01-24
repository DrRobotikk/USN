import java.util.ArrayList;

public class GeneriskStack<Type>{
    //Oppretter en Arraylist av Type:
    private ArrayList<Type> stakk = new ArrayList<>();

    //Metode for å returnere antall objekter i stakk:
    public int getSize() {
        return stakk.size();
    }

    //Metode for å teste om stakken er tom:
    public boolean isEmpty() {
        return stakk.isEmpty();
    }

    //Metode for å sette inn et nytt object:
    public void push(Type objekt) {
        stakk.add(objekt);
    }

    //Metode for å ta ut et objekt fra "øverst" (sist) i stakken:
    //Metoden skal også returnere objektet:
    public Type pop() {
        //Lager en huskereferanse til det siste objektet i stakken:
        Type t = stakk.get(stakk.size()-1);
        //Fjerner så objektet fra stakken ved å bruke ArrayList-metoden remove:
        stakk.remove(stakk.size()-1);
        //Så returnerer vi det objektet som har fått navnet t:
        return t;
    }

    public Type peep() {
        //Skal bare returnere en referanse til objektet:
        return stakk.get(stakk.size()-1);
    }

    //Metode for å returnere innholdet som en array:
    //Slik kan vi skrive ut hele innholdet i arrayen samt at vi definerer at stakken er en array
    public Object[] getInnhold() {
        return stakk.toArray();
    }


}
