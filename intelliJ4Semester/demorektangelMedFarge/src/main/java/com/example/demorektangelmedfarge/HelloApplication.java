package com.example.demorektangelmedfarge;

import javafx.application.Application;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.ListView;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;

import java.io.IOException;
import java.util.ArrayList;

public class HelloApplication extends Application {
    ListView liste;
    ArrayList<String> farger = new ArrayList<>();
    Rectangle rektangel;
    @Override
    public void start(Stage stage) throws IOException {

        try {
            BorderPane root = new BorderPane();
            VBox listepanel = new VBox();
            root.setLeft(listepanel);
            //Oppretter lista:
            liste = new ListView();
            //Legger til fargenavn i lista:
            farger.add("Rød");
            farger.add("Blå");
            farger.add("Gul");
            //Oppretter en observableList (kontrollen):
            ObservableList<String> innhold = FXCollections.observableArrayList();
            //Legger modellen (Arraylisten) inn i kontrollen:
            innhold.addAll(farger);
            //Kobler kontrollen med viewet (listView):
            liste.setItems(innhold);
            listepanel.getChildren().add(liste);
            //Trenger en knapp:
            Button knapp = new Button("Endre farge");
            //Kobler knappen til en lytter:
            knapp.setOnAction(e -> endreFarge());
            //Legger til knappen i panelet:
            listepanel.getChildren().add(knapp);
            //Oppretter et rektangel:
            rektangel = new Rectangle();
            //setter størrelse og fargene:
            rektangel.setX(150.0f);
            rektangel.setY(75.0f);
            rektangel.setWidth(200.0f);
            rektangel.setHeight(100.0f);
            rektangel.setFill(Color.RED);
            //Legger til rektangelet i panelet:
            root.setCenter(rektangel);
            Scene scene = new Scene(root, 520, 240);
            stage.setTitle("Rektangel med farge");
            stage.setScene(scene);
            stage.show();
        } catch (Exception e) {
            e.printStackTrace();
        }

    }
    public void endreFarge() {
        //Henter ut valgt farge som ObservableList:
        ObservableList valgtFarge = liste.getSelectionModel().getSelectedIndices();
        //I dette programmet har vi singel valg.
        //Valget ligger da på plass 0 i valgtFarge:
        //Det vi får er indeksen til valget i Arraylisten:
        int valgIndeks = (int) valgtFarge.get(0);
        //Henter ut fargen fra Arraylisten:
        String velgFarge = farger.get(valgIndeks);
        //Tester på valget:
        if (velgFarge.equals("Rød")) {
            behandleRod();
        } else if (velgFarge.equals("Blå")) {
            behandleBlaa();
        } else {
            behandleGul();
        }
    }
    public void behandleRod() {
        rektangel.setFill(Color.RED);
    }

    public void behandleBlaa() {
        rektangel.setFill(Color.BLUE);
    }

    public void behandleGul() {
        rektangel.setFill(Color.YELLOW);
    }
    public static void main(String[] args) {
        launch();
    }
}