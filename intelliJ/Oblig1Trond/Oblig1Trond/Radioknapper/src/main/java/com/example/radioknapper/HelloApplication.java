package com.example.radioknapper;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.RadioButton;
import javafx.scene.control.ToggleGroup;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

import java.io.IOException;

public class HelloApplication extends Application {
    //Et objekt av classen ToggleGroup kontrollerer
    //at bare en radioknapp kan hukes av:
    ToggleGroup gruppe = new ToggleGroup();
    //Deklarerer knapper:
    RadioButton rb1, rb2, rb3;
    @Override
    public void start(Stage stage) throws IOException {
        //lager en VBoks til plassering av radioknappene
        //Denne erstatter BorderPane:
        VBox root = new VBox();
        //Oppretter en knapp og setter den til default:
        rb1 = new RadioButton("OBJ2000");
        //Setter den til true som default
        rb1.setSelected(true);
        rb2 = new RadioButton("DAT2000");
        rb3 = new RadioButton("Surprise");
        //Knytter knappene til ToggleGroup:
        rb1.setToggleGroup(gruppe);
        rb2.setToggleGroup(gruppe);
        rb3.setToggleGroup(gruppe);
        //Legger knappene til rootPanelet:
        root.getChildren().addAll(rb1,rb2,rb3);
        //En annen måte å håndtere hendelser på (uten lytter):
        rb1.setOnAction(e -> {if (rb1.isSelected()) System.out.println("OBJ2000 ble valgt");});
        rb2.setOnAction(e -> {if (rb2.isSelected()) System.out.println("DAT2000 ble valgt");});
        rb3.setOnAction(e -> {if (rb3.isSelected()) System.out.println("Du er homo");});
        Scene scene = new Scene(root, 320, 240);
        stage.setTitle("Radioknapper");
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }
}