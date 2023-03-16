module com.example.demosceneskifterihundremeterskogen {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.demosceneskifterihundremeterskogen to javafx.fxml;
    exports com.example.demosceneskifterihundremeterskogen;
}