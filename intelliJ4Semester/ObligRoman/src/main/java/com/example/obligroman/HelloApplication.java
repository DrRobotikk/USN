package com.example.obligroman;

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
    MenuBar footer = new MenuBar();
    Menu filMeny = new Menu("Filmeny");
    Menu redigerMeny = new Menu("Rediger");
    Menu avsluttMeny = new Menu("Avslutt");
    MenuItem lagre = new MenuItem("Lagre");
    MenuItem lese = new MenuItem("Lese");
    //MenuItem avslutt = new MenuItem("Avslutt");
    MenuItem ny_vare = new MenuItem("Ny vare");
    MenuItem finn_vare = new MenuItem("Finn vare");
    MenuItem lag_faktura = new MenuItem("Lag faktura");
    MenuItem kontakt = new MenuItem("Kontakt med kunde");
    Stage primaerscene;
    @Override
    public void start(Stage stage) throws IOException {
        primaerscene = stage;
        BorderPane root = new BorderPane();

        //Lager menyen:
        filMeny.getItems().addAll(lagre, lese);
        //Legger Itemmenyen til menylinjen:
        menylinje.getMenus().add(filMeny);
        root.setTop(menylinje);
        root.setBottom(footer);
        footer.getMenus().add(avsluttMeny);
        avsluttMeny.setOnAction(e -> behandlerLagre());
        lagre.setOnAction(e -> behandlerLagre());
        lese.setOnAction(e -> behandlerLese());
        redigerMeny.getItems().addAll(ny_vare, finn_vare, lag_faktura, kontakt);
        menylinje.getMenus().add(redigerMeny);
        Scene scene = new Scene(root, 320, 240);
        stage.setTitle("Overskrift");
        stage.setScene(scene);
        stage.show();
    }

    public void behandlerLagre() {
        BorderPane lagreP = new BorderPane();
        Scene sceneLagre = new Scene(lagreP, 320, 240);
        MenuItem avslutt = new MenuItem("Avslutt");
        avsluttMeny.getItems().addAll(avslutt);
        menylinje.getMenus().add(avsluttMeny);
        System.out.println("Lagre");
        primaerscene.setScene(sceneLagre);
    }

    public void behandlerLese() {
        BorderPane leseP = new BorderPane();
        Scene sceneLese = new Scene(leseP, 320, 240);
        //Setter bakgrunnsfargen på panelet til gul:
        leseP.setBackground(new Background(new BackgroundFill(Color.YELLOW, new CornerRadii(0), Insets.EMPTY)));
        primaerscene.setScene(sceneLese);
    }

    public void behandlerAvslutt() {
        //Knappen avslutt skal lukke programmet:
        BorderPane avsluttP = new BorderPane();
        Scene sceneAvslutt = new Scene(avsluttP, 320, 240);
        //Setter bakgrunnsfargen på panelet til gul:
        avsluttP.setBackground(new Background(new BackgroundFill(Color.YELLOW, new CornerRadii(0), Insets.EMPTY)));
        primaerscene.setScene(sceneAvslutt);
    }

    public void tilbake() {
        //Knappen tilbake skal gå tilbake til hovedmenyen:
        BorderPane root = new BorderPane();
        Scene scene = new Scene(root, 320, 240);
        primaerscene.setScene(scene);
    }



    public static void main(String[] args) {
        launch();
    }
}