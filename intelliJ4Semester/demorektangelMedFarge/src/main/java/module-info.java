module com.example.demorektangelmedfarge {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.demorektangelmedfarge to javafx.fxml;
    exports com.example.demorektangelmedfarge;
}