module com.example.demotabellmedkundedb {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.demotabellmedkundedb to javafx.fxml;
    exports com.example.demotabellmedkundedb;
}