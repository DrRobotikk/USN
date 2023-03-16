package com.example.demolistboks;

import javafx.application.Application;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.ListView;
import javafx.scene.layout.BorderPane;
import javafx.stage.Stage;

import java.io.IOException;
import java.util.ArrayList;

public class HelloApplication extends Application {
    //Definerer en listebox:
    private ListView<String> listeboks;
    //Lager:
    private ArrayList<String> ukedager = new ArrayList<>();
    @Override
    public void start(Stage primaryStage) {
        try {

            primaryStage.setTitle("Demo av listekoks");
            //Lager listeboksen:
            listeboks = new ListView<>();
            //Legger til ukedagene:
            ukedager.add("Mandag");
            ukedager.add("Tirsdag");
            ukedager.add("Onsdag");
            ukedager.add("Torsdag");
            ukedager.add("Fredag");
            //Lager selve kontroll objektet:
            ObservableList<String> innhold = FXCollections.observableArrayList();
            //Legger Arraylisten med ukedagene inn i kontroll objektet:
            innhold.addAll(ukedager);
            //Knytter kontrollobjektet til listeboksen:
            listeboks.setItems(innhold);
            Button knapp = new Button("Legg til ukedag");
            //Knytter knappen til lytteren:
            knapp.setOnAction(e -> behandleValg());
            //Layouten:
            BorderPane root = new BorderPane();
            root.setCenter(listeboks);
            root.setBottom(knapp);



            //stage.setTitle("Hello!");
            //stage.setScene(scene);
            //stage.show();


        }catch (Exception e) {
            e.printStackTrace();
        }

    }

    public void behandleValg() {
        //Vi skal hente ut det som er valgt i listeboksen:
        //Dette skjer i form av en observableLIst
        ObservableList valgteElementer = listeboks.getSelectionModel().getSelectedIndices();
        //Siden vi har single selection, så er det bare ett objekt i valgteElementer!
        //Dette vil ha indeks 0:
        int indeks = (int) valgteElementer.get(0);
        //Vi bruker indeksen til å hente ut ukedagen
        //fra den opprinnelige arraylisten ukedager:
        System.out.println(ukedager.get(indeks));
        //JOptionPane.showMessageDialog(null, ukedager.get(indeks));
    }

    public static void main(String[] args) {
        launch();
    }
}