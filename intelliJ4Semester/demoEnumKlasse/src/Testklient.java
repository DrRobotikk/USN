public class Testklient {
    public static void main(String[] args) {
        Ansatt a1 = new Ansatt("Ole", Ansettelsesforhold.FAST);
        Ansatt a2 = new Ansatt("Lise", Ansettelsesforhold.PROSJEKT);

        System.out.println(a1.getNavn());
        System.out.println(a1.getStatus());
        System.out.println(a1.toString());
        System.out.println(a2.getNavn());
        System.out.println(a2.getStatus());
        System.out.println(a2.toString());
    }
}
