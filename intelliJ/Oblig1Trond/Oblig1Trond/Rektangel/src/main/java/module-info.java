module com.example.rektangel {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.rektangel to javafx.fxml;
    exports com.example.rektangel;
}