module com.example.obligroman {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.obligroman to javafx.fxml;
    exports com.example.obligroman;
}