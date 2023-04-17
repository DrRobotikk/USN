module com.example.obligroman {
    requires javafx.controls;
    requires javafx.fxml;
    requires javafx.base;


    opens com.example.obligroman to javafx.fxml;


    exports com.example.obligroman.domeneklasser;

    opens com.example.obligroman.Grensesnitt to javafx.fxml;
    exports com.example.obligroman.Grensesnitt;

}