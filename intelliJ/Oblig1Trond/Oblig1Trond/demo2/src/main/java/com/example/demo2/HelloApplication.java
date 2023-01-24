package com.example.demo2;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.ComboBox;
import javafx.scene.layout.BorderPane;
import javafx.stage.Stage;

import java.io.IOException;

public class HelloApplication extends Application {
    ComboBox<String> liste;

    String[] alts = {"Mandag","Tirsdag","Onsdag","Torsdag","Fredag","Lørdag","Søndag"};

    @Override
    public void start(Stage stage) throws IOException {

        liste = new ComboBox<String>();
        liste.getItems().addAll(alts);
        //Setter overskrift på komboboksen:
        liste.setValue("Ukedag");
        //Knytter komboboksen til lytteren:
        liste.setOnAction(e -> behandleValg());
        BorderPane root = new BorderPane();
        root.setCenter(liste);
        Scene scene = new Scene(root, 320, 240);
        stage.setTitle("Ukedager");
        stage.setScene(scene);
        stage.show();

    }

    public void behandleValg() {
        String valg = liste.getValue();
        System.out.println("Du valgte " + valg);
    }

    public static void main(String[] args) {
        launch();
    }
}