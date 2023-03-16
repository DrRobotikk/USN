package com.example.demoenumogkombobox;

public enum Ansettelsesforhold {
    FAST, MIDLERTIDIG, PROSJEKT, SLUTTET;

    public String toString() {
        //Tester på verdien:
        switch (this) {
            case FAST:
                return "Fast ansatt";
            case MIDLERTIDIG:
                return "Midlertidig ansatt";
            case PROSJEKT:
                return "Prosjektansatt";
            case SLUTTET:
                return "Sluttet";
            default:
                return "Ukjent";
        }
    }
}
