module com.example.demolistboksny {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.demolistboksny to javafx.fxml;
    exports com.example.demolistboksny;
}