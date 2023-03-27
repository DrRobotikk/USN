module com.example.obligromankollar {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.domeneklasser to javafx.fxml;
    exports com.example.domeneklasser;
    exports domeneklasser;
    opens domeneklasser to javafx.fxml;
    exports grensesnitt;
    opens grensesnitt to javafx.fxml;
}