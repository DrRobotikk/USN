package com.example.demosceneskifterihundremeterskogen;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;

public class HelloApplication extends Application {

    private Stage vindu;
    private Scene scene1, scene2;
    private TabelView tabell;
    private TextField txtNavn, txtAdresse, txtTelefon;
    //ObservableList for person-objecter:
    private ObservableList<Person> data = FXCollections.observableArrayList(
            new Person("Ole Brum","Hundremeterskogen 1","123"),
            new Person("Nasse Nøff","Hundremeterskogen 2","456"));

    @Override
    public void start(Stage stage) throws IOException {
        vindu = stage;
        lagScene1();
    }

    public void lagScene1() {
        BorderPane rotpanel = new BorderPane();
        scene1 = new Scene(rotpanel, 400, 300);
        vindu.setTitle("Enkel tabell");
        vindu.setWidth(400);
        vindu.setHeight(300);
        //legger til en tabell:
        tabell = new TableView();
        TableColumn kolNavn = new TableColumn<>("Navn:");
        kolNavn.setMinWidth(100);
        kolNavn.setCellValueFactory(new PropertyValueFactory<Person, String>("navn"));
        TableColumn kolAdresse = new TableColumn<>("Adresse:");
        kolAdresse.setMinWidth(100);
        kolAdresse.setCellValueFactory(new PropertyValueFactory<Person, String>("adresse"));
        TableColumn kolTelefon = new TableColumn<>("Telefon:");
        kolTelefon.setMinWidth(100);
        kolTelefon.setCellValueFactory(new PropertyValueFactory<Person, String>("telefon"));
        lagScene2();
        Button ny = new Button("Ny person");
        ny.setOnAction(e -> vindu.setScene(scene2));
        tabell.getColumns().addAll(kolNavn, kolAdresse, kolTelefon);
        tabell.setItems(data);
        rotpanel.setCenter(tabell);
        rotpanel.setBottom(ny);
        vindu.show();
    }

    public void lagScene2() {
        GridPane layout2 = new GridPane();
    }

    public static void main(String[] args) {
        launch();
    }
}