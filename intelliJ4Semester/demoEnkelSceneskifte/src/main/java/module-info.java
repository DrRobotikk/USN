module com.example.demoenkelsceneskifte {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.demoenkelsceneskifte to javafx.fxml;
    exports com.example.demoenkelsceneskifte;
}