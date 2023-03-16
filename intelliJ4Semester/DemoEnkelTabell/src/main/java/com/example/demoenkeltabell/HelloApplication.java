package com.example.demoenkeltabell;

import javafx.application.Application;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.layout.BorderPane;
import javafx.stage.Stage;

import java.io.IOException;

public class HelloApplication extends Application {

    private TableView tabell = new TableView();
    //Lager et ObservableList objekt med data:
    private ObservableList<Person> data = FXCollections.observableArrayList(
            new Person("Ole", "Vei 2", "123"),
            new Person("Lise", "Gate 5", "456"),
            new Person("Kari", "Vei 8", "789")
    );
    @Override
    public void start(Stage stage) throws IOException {
        BorderPane root = new BorderPane();
        Scene scene = new Scene(root,400, 400);
        stage.setTitle("Enkel tabell");
        //Oppretter tabellkolonner:
        TableColumn colNavn = new TableColumn("Navn:");
        //Setter minimums bredde på kolonnen:
        colNavn.setMinWidth(100);
        //Vi trenger et objekt som skal hente ut navnene fra personobjektene:
        colNavn.setCellValueFactory(
                new PropertyValueFactory<Person, String>("navn")
        );
        //Neste kolonne:
        TableColumn colAdresse = new TableColumn("Adresse:");
        //Setter minimums bredde på kolonnen:
        colAdresse.setMinWidth(100);
        //Vi trenger et objekt som skal hente ut adressene fra personobjektene:
        colAdresse.setCellValueFactory(
                new PropertyValueFactory<Person, String>("adresse")
        );
        TableColumn colTlf = new TableColumn("Tlf:");
        //Setter minimums bredde på kolonnen:
        colTlf.setMinWidth(100);
        //Vi trenger et objekt som skal hente ut telefonnummer fra personobjektene:
        colTlf.setCellValueFactory(
                new PropertyValueFactory<Person, String>("telefon")
        );
        //Legger til kolonnene i tabellen:
        tabell.getColumns().addAll(colNavn, colAdresse, colTlf);
        //Legger til personene i ObservableLIst:
        tabell.setItems(data);
        root.setCenter(tabell);

        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }
}