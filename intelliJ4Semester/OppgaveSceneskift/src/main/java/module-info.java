module com.example.oppgavesceneskift {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.oppgavesceneskift to javafx.fxml;
    exports com.example.oppgavesceneskift;
}