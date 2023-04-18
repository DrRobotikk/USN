package com.example.obligroman.Grensesnitt;


import com.example.obligroman.Kontroll.Kontroll;
import com.example.obligroman.domeneklasser.*;
import javafx.application.Application;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.scene.text.Font;
import javafx.scene.text.FontWeight;
import javafx.scene.text.Text;
import javafx.stage.Stage;

import java.io.IOException;

public class HelloApplication extends Application {
    Kontroll kontroll = new Kontroll();


    //DEFINERER MENYEN:
    MenuBar menylinje = new MenuBar();
    Menu kundeMeny = new Menu("Kundebehandling");
    Menu fakturaMeny = new Menu("Fakturabehandling");
    Menu vareMeny = new Menu("Varebehandling");
    MenuItem privatKundeItem = new MenuItem("Registrer ny privatkunde");
    MenuItem firmaKundeItem = new MenuItem("Registrer ny firmakunde");
    MenuItem kontaktItem = new MenuItem("Kontakt med kunde");
    MenuItem lagFakturaItem = new MenuItem("Ny faktura");
    MenuItem lagFakturaLinjeItem = new MenuItem("Ny fakturalinje");
    MenuItem visFakturaItem = new MenuItem("Vis faktura");
    MenuItem nyVareItem = new MenuItem("Ny vare");
    Button lagreKnapp = new Button("Lagre");
    Button tilbake = new Button("Tilbake");

    //DEFINERER SCENER OG STAGE:
    private Scene primaryScene, nyVareScene, nyPrivatKundeScene, nyFirmaKundeScene, visVareScene, lagFakturaScene, kontaktScene;
    private Stage primaryStage;

    @Override
    public void start(Stage primaryStage) throws IOException {

        try {
            // Setter primærscenen
            this.primaryStage = primaryStage;
            BorderPane root = new BorderPane();
            Label infotekst = new Label("Velkommen til Kunde- og varebehandlinssystemet.");
            //Lager menyene:
            kundeMeny.getItems().addAll(privatKundeItem, firmaKundeItem, kontaktItem);
            fakturaMeny.getItems().addAll(lagFakturaItem, lagFakturaLinjeItem, visFakturaItem);
            vareMeny.getItems().addAll(nyVareItem);
            //Legger ItemMenyene til navbaren:
            menylinje.getMenus().addAll(kundeMeny, fakturaMeny, vareMeny);
            //Angir positionen til navbaren:
            root.setTop(menylinje);
            root.setCenter(infotekst);
            //Angir hva som skal skje når man trykker på menyene:
            privatKundeItem.setOnAction(e -> behandlerPrivatkundeItem());
            firmaKundeItem.setOnAction(e -> behandlerFirmakundeItem());
            nyVareItem.setOnAction(e -> behandlerNyVareItem());
            lagFakturaItem.setOnAction(e -> behandlerLagFakturaItem());
            lagFakturaLinjeItem.setOnAction(e -> behandlerLagFakturaLinjeItem());
            kontaktItem.setOnAction(e -> behandlerKontaktItem());
            visFakturaItem.setOnAction(e -> behandleVisFakturaItem());
            //Angir primærscenen:
            primaryScene = new Scene(root, 600, 400);
            primaryStage.setTitle("Kunde- og varebehandlingssystem");
            primaryStage.setScene(primaryScene);
            primaryStage.show();
            //Avslutt knappen:
            Button avslutt = new Button("Avslutt");
            avslutt.setOnAction(e -> avslutt());
            root.setBottom(avslutt);
            BorderPane.setAlignment(avslutt, Pos.BOTTOM_RIGHT);
            kontroll.lese();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    // Håndterer registreringen av nye privatkunder
    public void behandlerPrivatkundeItem() {
        Label privatkundeLabel = new Label("Registrer ny privatkunde.");
        privatkundeLabel.setFont(Font.font("Arial", FontWeight.BOLD, 14));
        Label kundenavnLabel = new Label("Oppgi navn:");
        Label butikkLabel = new Label("Oppgi butikk:");
        TextField kundenavn = new TextField();
        TextField kundebutikk = new TextField();
        // Oppretter hbox for kundenr og kundenavn
        HBox row2 = new HBox(20, kundenavnLabel, kundenavn);
        HBox row3 = new HBox(10, butikkLabel, kundebutikk);
        row2.setAlignment(Pos.BASELINE_CENTER);
        row3.setAlignment(Pos.BASELINE_CENTER);
        lagreKnapp = new Button("Lagre");
        lagreKnapp.setOnAction(e -> {
            Privatkunde kunde = new Privatkunde(kontroll.generererkundenr(), kundenavn.getText(), kundebutikk.getText());
            kontroll.nyKunde(kunde);
            kundenavn.clear();
            kundebutikk.clear();
        });
        tilbake = new Button("Tilbake");
        tilbake.setOnAction(e -> primaryStage.setScene(primaryScene));
        VBox kundeBoks = new VBox();
        kundeBoks.getChildren().addAll(row2, row3);
        kundeBoks.setAlignment(Pos.CENTER_LEFT);
        BorderPane nyKundeP = new BorderPane();
        nyKundeP.setTop(privatkundeLabel);
        nyKundeP.setCenter(kundeBoks);
        nyKundeP.setBottom(tilbake);
        nyKundeP.setRight(lagreKnapp);
        BorderPane.setAlignment(lagreKnapp, Pos.BOTTOM_CENTER);
        BorderPane.setAlignment(tilbake, Pos.BOTTOM_RIGHT);
        nyPrivatKundeScene = new Scene(nyKundeP, 600, 400);
        primaryStage.setScene(nyPrivatKundeScene);
    }

    public void behandlerFirmakundeItem() {
        Label firmakundeLabel = new Label("Registrer ny firmakunde.");
        firmakundeLabel.setFont(Font.font("Arial", FontWeight.BOLD, 14));
        Label kundenavnLabel = new Label("Oppgi navn:");
        Label kredittLabel = new Label("Oppgi kredittgrense:");
        Label telefonnrLabel = new Label("Oppgi telefonnr:");
        TextField kundenavn = new TextField();
        TextField kundekreditt = new TextField();
        TextField kundetelefonnr = new TextField();
        // Oppretter hbox for kundenr og kundenavn
        HBox row2 = new HBox(55, kundenavnLabel, kundenavn);
        HBox row3 = new HBox(10, kredittLabel, kundekreditt);
        HBox row4 = new HBox(32, telefonnrLabel, kundetelefonnr);
        row2.setAlignment(Pos.BASELINE_CENTER);
        row3.setAlignment(Pos.BASELINE_CENTER);
        row4.setAlignment(Pos.BASELINE_CENTER);
        lagreKnapp = new Button("Lagre");
        lagreKnapp.setOnAction(e -> {
            Firmakunde kunde = new Firmakunde(kontroll.generererkundenr(), kundenavn.getText(), Double.parseDouble(kundekreditt.getText()), kundetelefonnr.getText());
            kontroll.nyKunde(kunde);
            kundenavn.clear();
            kundekreditt.clear();
            kundetelefonnr.clear();
        });
        tilbake = new Button("Tilbake");
        tilbake.setOnAction(e -> primaryStage.setScene(primaryScene));
        VBox kundeBoks = new VBox();
        kundeBoks.getChildren().addAll(row2, row3, row4);
        kundeBoks.setAlignment(Pos.CENTER_LEFT);
        BorderPane nyKundeF = new BorderPane();
        nyKundeF.setTop(firmakundeLabel);
        nyKundeF.setCenter(kundeBoks);
        nyKundeF.setBottom(tilbake);
        nyKundeF.setRight(lagreKnapp);
        BorderPane.setAlignment(lagreKnapp, Pos.BOTTOM_CENTER);
        BorderPane.setAlignment(tilbake, Pos.BOTTOM_RIGHT);
        nyFirmaKundeScene = new Scene(nyKundeF, 600, 400);
        primaryStage.setScene(nyFirmaKundeScene);
    }


    // Håndterer registreringen av nye varer
    public void behandlerNyVareItem() {
        Label nyVareLabel = new Label("Registrer ny vare.");
        nyVareLabel.setFont(Font.font("Arial", FontWeight.BOLD, 14));
        Label varenrLabel = new Label("Oppgi varenummer:");
        Label varenavnLabel = new Label("Oppgi varenavn:");
        Label vareprisLabel = new Label("Oppgi varepris:");
        TextField varenr = new TextField();
        TextField varenavn = new TextField();
        TextField varepris = new TextField();
        HBox row1 = new HBox(10, varenrLabel, varenr);
        HBox row2 = new HBox(30, varenavnLabel, varenavn);
        HBox row3 = new HBox(35, vareprisLabel, varepris);
        row1.setAlignment(Pos.BASELINE_CENTER);
        row2.setAlignment(Pos.BASELINE_CENTER);
        row3.setAlignment(Pos.BASELINE_CENTER);
        VBox varerBoks = new VBox();
        varerBoks.getChildren().addAll(row1, row2, row3);
        varerBoks.setAlignment(Pos.CENTER_LEFT);
        lagreKnapp = new Button("Lagre");
        lagreKnapp.setOnAction(e -> {
            Vare vare = new Vare(varenr.getText(), varenavn.getText(), Double.parseDouble(varepris.getText()));
            kontroll.nyVare(vare);
            varenr.clear();
            varenavn.clear();
            varepris.clear();
        });
        tilbake = new Button("Tilbake");
        tilbake.setOnAction(e -> primaryStage.setScene(primaryScene));
        BorderPane nyVareP = new BorderPane();
        nyVareP.setTop(nyVareLabel);
        nyVareP.setCenter(varerBoks);
        nyVareP.setBottom(tilbake);
        nyVareP.setRight(lagreKnapp);
        BorderPane.setAlignment(lagreKnapp, Pos.BOTTOM_CENTER);
        BorderPane.setAlignment(tilbake, Pos.BOTTOM_RIGHT);
        nyVareScene = new Scene(nyVareP, 600, 400);
        primaryStage.setScene(nyVareScene);
    }

    // Håndterer registrering av faktura
    public void behandlerLagFakturaItem() {
        //Instansierer klasser:
        Label lagFakturaLabel = new Label("Lag faktura");
        lagFakturaLabel.setFont(Font.font("Arial", FontWeight.BOLD, 14));
        Label kundenrlbl = new Label("Oppgi kundenr:");
        Label fakturadatoLable = new Label("Oppgi fakturadato (dd-MM-yyyy");
        Label forfallsdatoLabel = new Label("Oppgi forfallsdato (dd-MM-yyyy");
        TextField kundenr = new TextField();
        TextField fakturadato = new TextField();
        TextField forfallsdato = new TextField();
        Button opprett = new Button("Opprett faktura");
        tilbake = new Button("Tilbake");
        //Setter data inn i bokser og scener:
        HBox row1 = new HBox(102, kundenrlbl, kundenr);
        HBox row2 = new HBox(10, fakturadatoLable, fakturadato);
        HBox row3 = new HBox(10, forfallsdatoLabel, forfallsdato);
        row1.setAlignment(Pos.BASELINE_CENTER);
        row2.setAlignment(Pos.BASELINE_CENTER);
        row3.setAlignment(Pos.BASELINE_CENTER);
        VBox fakturaboks = new VBox();
        fakturaboks.getChildren().addAll(row1, row2, row3);
        fakturaboks.setAlignment(Pos.CENTER_LEFT);
        //Setter lamda funksjoner for knapper:
        tilbake.setOnAction(e -> primaryStage.setScene(primaryScene));
        opprett.setOnAction(e -> {
            kontroll.nyFaktura(kundenr.getText(), fakturadato.getText(), forfallsdato.getText());
            kundenr.clear();
            fakturadato.clear();
            forfallsdato.clear();
        });
        // Oppretter borderpane til å holde alle UI elementene
        BorderPane lagFakturaP = new BorderPane();
        lagFakturaP.setTop(lagFakturaLabel);
        lagFakturaP.setCenter(fakturaboks);
        lagFakturaP.setBottom(tilbake);
        lagFakturaP.setRight(lagreKnapp);
        BorderPane.setAlignment(lagreKnapp, Pos.BOTTOM_CENTER);
        BorderPane.setAlignment(tilbake, Pos.BOTTOM_RIGHT);
        // Lager scenen med borderpanen og setter den til primærscenen
        lagFakturaScene = new Scene(lagFakturaP, 600, 400);
        primaryStage.setScene(lagFakturaScene);
    }

    public void behandleVisFakturaItem() {
        Label lagFakturaLabel = new Label("Vis faktura");
        Label fakturanrlbl = new Label("Oppgi fakturanr:");
        TextField fakturanr = new TextField();
        Button vis = new Button("Vis faktura");
        tilbake = new Button("Tilbake");
        //Oppretter tableview med kolonner:
        TableView fakturalinjer = new TableView<>();
        TableColumn column1 = new TableColumn<>("Varenummer:");
        column1.setCellValueFactory(new PropertyValueFactory<Fakturalinje, String>("varenr"));
        column1.setMinWidth(100);
        TableColumn column2 = new TableColumn<>("Varenavn:");
        column2.setMinWidth(200);
        column2.setCellValueFactory(new PropertyValueFactory<Fakturalinje, String>("varenavn"));
        TableColumn column3 = new TableColumn<>("Antall:");
        column3.setMinWidth(100);
        column3.setCellValueFactory(new PropertyValueFactory<Fakturalinje, Integer>("antall"));
        TableColumn column4 = new TableColumn<>("Rabatt:");
        column4.setMinWidth(100);
        column4.setCellValueFactory(new PropertyValueFactory<Fakturalinje, Double>("rabatt"));
        TableColumn column5 = new TableColumn<>("Totalpris:");
        column5.setMinWidth(100);
        column5.setCellValueFactory(new PropertyValueFactory<Fakturalinje, Double>("totalPris"));
        fakturalinjer.getColumns().addAll(column1, column2, column3, column4, column5);
        //Setter data inn i bokser og scener:
        HBox fakturaboks = new HBox(10, fakturanrlbl, fakturanr, vis);
        fakturaboks.setAlignment(Pos.CENTER_LEFT);
        //Setter lamda funksjoner for knapper:
        tilbake.setOnAction(e -> primaryStage.setScene(primaryScene));
        vis.setOnAction(e -> fakturalinjer.setItems(kontroll.finnFakturalinje(fakturanr.getText())));
        // Oppretter borderpane til å holde alle UI elementene
        BorderPane lagFakturaP = new BorderPane();
        lagFakturaP.setCenter(lagFakturaLabel);
        lagFakturaP.setTop(fakturaboks);
        lagFakturaP.setCenter(fakturalinjer);
        lagFakturaP.setBottom(tilbake);
        BorderPane.setAlignment(tilbake, Pos.BOTTOM_RIGHT);
        // Lager scenen med borderpanen og setter den til primærscenen
        lagFakturaScene = new Scene(lagFakturaP, 600, 400);
        primaryStage.setScene(lagFakturaScene);
    }


    // Metode for å håndtere registrering av en ny fakturalinje
    public void behandlerLagFakturaLinjeItem() {

        Label lagFakturaLabel = new Label("Lag fakturalinje");
        lagFakturaLabel.setFont(Font.font("Arial", FontWeight.BOLD, 14));
        Label spacing = new Label(" ");
        Label spacing2 = new Label(" ");
        tilbake = new Button("Tilbake");
        Button hent = new Button("Hent Kundeinfo");
        lagreKnapp = new Button("Lagre");
        Label kundenrLabel = new Label("Oppgi Kundenr:");
        TextField kundenr = new TextField();
        HBox row1 = new HBox(20, kundenrLabel, kundenr);
        VBox innlesningsfelt = new VBox(lagFakturaLabel,spacing,row1,spacing2, hent);
        BorderPane lagFakturaP = new BorderPane();
        tilbake.setOnAction(e -> primaryStage.setScene(primaryScene));
        hent.setOnAction(e -> {
            if (kontroll.rabattKunde(kundenr.getText())) {

                genererForFirma(lagFakturaP,lagreKnapp);

            } else {
                genererForPrivat(lagFakturaP,lagreKnapp);
            }
            ;
        });

        lagFakturaP.setTop(innlesningsfelt);
        //lagFakturaP.setTop(lagFakturaLabel);

        lagFakturaP.setBottom(tilbake);
        lagFakturaP.setRight(lagreKnapp);
        BorderPane.setAlignment(lagreKnapp, Pos.BOTTOM_CENTER);
        BorderPane.setAlignment(tilbake, Pos.BOTTOM_RIGHT);
        lagFakturaScene = new Scene(lagFakturaP, 600, 400);
        primaryStage.setScene(lagFakturaScene);
    }

    private BorderPane genererForPrivat(BorderPane lagFakturaP,Button lagreKnapp) {
        Label fakturanrLabel = new Label("Fakturanr:");
        Label varenrLabel = new Label("Varenr:");
        Label antallLabel = new Label("Antall:");
        TextField fakturanr = new TextField();
        TextField varenr = new TextField();
        TextField antall = new TextField();
        HBox fakturaBox = new HBox(10, fakturanrLabel,fakturanr);
        HBox varenrBox = new HBox(24, varenrLabel, varenr);
        HBox antallBox = new HBox(28, antallLabel, antall);
        fakturaBox.setAlignment(Pos.BASELINE_CENTER);
        varenrBox.setAlignment(Pos.BASELINE_CENTER);
        antallBox.setAlignment(Pos.BASELINE_CENTER);
        VBox fakturalinje = new VBox(fakturaBox,varenrBox, antallBox);
        fakturalinje.setAlignment(Pos.CENTER_LEFT);
        lagFakturaP.setCenter(fakturalinje);
        lagreKnapp.setOnAction(e -> {
            kontroll.nyFakturalinje(fakturanr.getText(), varenr.getText(), antall.getText(),"0");
            fakturanr.clear();
            varenr.clear();
            antall.clear();
        });

        return lagFakturaP;
    }

    private BorderPane genererForFirma(BorderPane lagFakturaP, Button lagreKnapp) {
        Label fakturanrLabel = new Label("Fakturanr:");
        Label varenrLabel = new Label("Varenr:");
        Label antallLabel = new Label("Antall:");
        Label rabatLabel = new Label("Rabatt:");
        TextField fakturanr = new TextField();
        TextField varenr = new TextField();
        TextField antall = new TextField();
        TextField rabatt = new TextField();
        HBox fakturaBox = new HBox(10, fakturanrLabel,fakturanr);
        HBox varenrBox = new HBox(24, varenrLabel, varenr);
        HBox antallBox = new HBox(28, antallLabel, antall);
        HBox rabattBox = new HBox(25, rabatLabel, rabatt);
        fakturaBox.setAlignment(Pos.BASELINE_CENTER);
        varenrBox.setAlignment(Pos.BASELINE_CENTER);
        antallBox.setAlignment(Pos.BASELINE_CENTER);
        rabattBox.setAlignment(Pos.BASELINE_CENTER);
        VBox fakturalinje = new VBox(fakturaBox,varenrBox, antallBox, rabattBox);
        fakturalinje.setAlignment(Pos.CENTER_LEFT);

        lagFakturaP.setCenter(fakturalinje);
        lagreKnapp.setOnAction(e -> {
            kontroll.nyFakturalinje(fakturanr.getText(), varenr.getText(), antall.getText(),rabatt.getText());
            fakturanr.clear();
            varenr.clear();
            antall.clear();
            rabatt.clear();
        });

        return lagFakturaP;
    }


    // Håndterer registrering av kontakt med kunde
    public void behandlerKontaktItem() {
        Label kontaktLabel = new Label("Kontakt med kunde");
        kontaktLabel.setFont(Font.font("Arial", FontWeight.BOLD, 14));
        lagreKnapp = new Button("Lagre");
        tilbake = new Button("Tilbake");
        tilbake.setOnAction(e -> primaryStage.setScene(primaryScene));
        BorderPane kontaktP = new BorderPane();
        kontaktP.setTop(kontaktLabel);
        kontaktP.setBottom(tilbake);
        kontaktP.setRight(lagreKnapp);
        BorderPane.setAlignment(lagreKnapp, Pos.BOTTOM_CENTER);
        BorderPane.setAlignment(tilbake, Pos.BOTTOM_RIGHT);
        VBox kontaktVB = new VBox();

        Label kundenrL = new Label("Kundenr:");
        TextField kundenr = new TextField();
        Label datoL = new Label("Dato:");
        TextField dato = new TextField();
        Label tekstL = new Label("Tekst:");
        TextField tekst = new TextField();

        HBox kundenrHB = new HBox(10, kundenrL, kundenr);
        HBox datoHB = new HBox(30, datoL, dato);
        HBox tekstHB = new HBox(29, tekstL, tekst);
        kundenrHB.setAlignment(Pos.BASELINE_CENTER);
        datoHB.setAlignment(Pos.BASELINE_CENTER);
        tekstHB.setAlignment(Pos.BASELINE_CENTER);
        kontaktVB.getChildren().addAll(kundenrHB, datoHB, tekstHB);
        kontaktVB.setAlignment(Pos.CENTER_LEFT);
        kontaktP.setCenter(kontaktVB);

        lagreKnapp.setOnAction(e -> {
            kontroll.nyKundekontakt(new Kundekontakt(kundenr.getText(), dato.getText(), tekst.getText()));
            kundenr.clear();
            dato.clear();
            tekst.clear();
        });
        kontaktScene = new Scene(kontaktP, 600, 400);
        primaryStage.setScene(kontaktScene);
    }


    // Lagrer alt og avslutter programkjøring
    public void avslutt() {
        kontroll.lagre();
        System.exit(0);
    }


    public static void main(String[] args) {
        launch();
    }
}