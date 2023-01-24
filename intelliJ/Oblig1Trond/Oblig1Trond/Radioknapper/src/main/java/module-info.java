module com.example.radioknapper {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.radioknapper to javafx.fxml;
    exports com.example.radioknapper;
}