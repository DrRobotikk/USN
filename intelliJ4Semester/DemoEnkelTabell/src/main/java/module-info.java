module com.example.demoenkeltabell {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.demoenkeltabell to javafx.fxml;
    exports com.example.demoenkeltabell;
}