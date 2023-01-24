package com.example.rektangel;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.layout.BorderPane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;

import java.io.IOException;

public class HelloApplication extends Application {

    Rectangle rektangel;
    @Override
    public void start(Stage stage) throws IOException {
        BorderPane root = new BorderPane();
        rektangel = new Rectangle();
        rektangel.setX(150.0f);
        rektangel.setY(75.0f);
        rektangel.setWidth(200.0f);
        rektangel.setHeight(100.0f);

        Scene scene = new Scene(root, 320, 240);
        rektangel.setFill(Color.RED);
        stage.setTitle("Rektangel");
        stage.setScene(scene);
        root.setCenter(rektangel);
        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }
}