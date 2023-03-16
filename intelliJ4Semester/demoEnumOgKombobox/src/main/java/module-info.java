module com.example.demoenumogkombobox {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.demoenumogkombobox to javafx.fxml;
    exports com.example.demoenumogkombobox;
}