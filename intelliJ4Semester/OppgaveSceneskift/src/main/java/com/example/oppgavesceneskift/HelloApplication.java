package com.example.oppgavesceneskift;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.Menu;
import javafx.scene.control.MenuBar;
import javafx.scene.control.MenuItem;
import javafx.scene.layout.Background;
import javafx.scene.layout.BackgroundFill;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.CornerRadii;
import javafx.scene.paint.Color;
import javafx.stage.Stage;

import java.io.IOException;

public class HelloApplication extends Application {
    MenuBar menylinje = new MenuBar();
    Menu fargemeny = new Menu("Farge");
    MenuItem rod = new MenuItem("Rød");
    MenuItem gul = new MenuItem("Gul");
    MenuItem blaa = new MenuItem("Blå");
    Stage primaerscene;
    @Override
    public void start(Stage stage) throws IOException {
        primaerscene = stage;
        BorderPane root = new BorderPane();
        //Lager menyen:
        fargemeny.getItems().addAll(rod, gul, blaa);
        //Legger fargemenyen til menylinjen:
        menylinje.getMenus().add(fargemeny);
        root.setTop(menylinje);
        rod.setOnAction(e -> behandlerod());
        gul.setOnAction(e -> behandlergul());
        blaa.setOnAction(e -> behandlerblaa());
        Scene scene = new Scene(root, 400, 400);
        stage.setTitle("Scene skift");
        stage.setScene(scene);
        stage.show();
    }

    public void behandlerod() {
        BorderPane rodP = new BorderPane();
        Scene sceneRod = new Scene(rodP, 400, 400);
        //Setter bakgrunnsfargen på panelet til rød:
        rodP.setBackground(new Background(new BackgroundFill(Color.RED, new CornerRadii(0), Insets.EMPTY)));
        primaerscene.setScene(sceneRod);
    }

    public void behandlergul() {
        BorderPane gulP = new BorderPane();
        Scene sceneGul = new Scene(gulP, 400, 400);
        //Setter bakgrunnsfargen på panelet til gul:
        gulP.setBackground(new Background(new BackgroundFill(Color.YELLOW, new CornerRadii(0), Insets.EMPTY)));
        primaerscene.setScene(sceneGul);
    }

    public void behandlerblaa() {
        BorderPane blaaP = new BorderPane();
        Scene sceneBlaa = new Scene(blaaP, 400, 400);
        //Setter bakgrunnsfargen på panelet til blå:
        blaaP.setBackground(new Background(new BackgroundFill(Color.BLUE, new CornerRadii(0), Insets.EMPTY)));
        primaerscene.setScene(sceneBlaa);
    }

    public static void main(String[] args) {
        launch();
    }
}