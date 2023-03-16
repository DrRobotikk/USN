module com.example.demolistboks {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.demolistboks to javafx.fxml;
    exports com.example.demolistboks;
}