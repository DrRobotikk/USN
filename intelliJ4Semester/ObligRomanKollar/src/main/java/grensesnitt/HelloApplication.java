package grensesnitt;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Menu;
import javafx.scene.control.MenuBar;
import javafx.scene.control.MenuItem;
import javafx.scene.layout.Background;
import javafx.scene.layout.BackgroundFill;
import javafx.scene.layout.BorderPane;
import javafx.scene.paint.Color;
import javafx.stage.Stage;

import java.io.IOException;

public class HelloApplication extends Application {

    MenuBar menylinje = new MenuBar();
    Menu meny = new Menu("Meny");
    MenuItem item1 = new MenuItem("Item 1");
    MenuItem item2 = new MenuItem("Item 2");
    MenuItem item3 = new MenuItem("Item 3");
    Stage primaerscene;
    @Override
    public void start(Stage stage) throws IOException {
        primaerscene = stage;
        BorderPane root = new BorderPane();
        //Lager menyen:
        meny.getItems().addAll(item1, item2, item3);
        //Legger Itemmenyen til menylinjen:
        menylinje.getMenus().add(meny);
        root.setTop(menylinje);
        item1.setOnAction(e -> behandlerItem1());
        item2.setOnAction(e -> behandlerItem2());
        item3.setOnAction(e -> behandlerItem3());
        Scene scene = new Scene(root, 320, 240);
        stage.setTitle("HOMO");
        stage.setScene(scene);
        stage.show();
    }

    public void behandlerItem1() {
        BorderPane item1P = new BorderPane();
        Scene sceneItem1 = new Scene(item1P, 320, 240);
        //Setter bakgrunnsfargen på panelet til rød:
        item1P.setBackground(new BackgroundFill(Color.RED, 0, 0));
        primaerscene.setScene(sceneItem1);
    }

    public void behandlerItem2() {
        BorderPane item2P = new BorderPane();
        Scene sceneItem2 = new Scene(item2P, 320, 240);
        //Setter bakgrunnsfargen på panelet til gul:
        item2P.setBackground(new BackgroundFill(Color.YELLOW, 0, 0));
        primaerscene.setScene(sceneItem2);
    }

    public void behandlerItem3() {
        BorderPane item3P = new BorderPane();
        Scene sceneItem3 = new Scene(item3P, 320, 240);
        //Setter bakgrunnsfargen på panelet til gul:
        item3P.setBackground(new BackgroundFill(Color.BLUE, 0, 0));
        primaerscene.setScene(sceneItem3);
    }

    public static void main(String[] args) {
        launch();
    }
}