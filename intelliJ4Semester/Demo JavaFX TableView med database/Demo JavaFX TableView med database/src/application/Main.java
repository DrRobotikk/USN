package application;
	
import java.sql.ResultSet;

import javafx.application.Application;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.TextField;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.FlowPane;


public class Main extends Application {
	Kontroll kontroll = new Kontroll();
	//Lager tabellen
	private TableView tabell = new TableView<>();
	//deklarerer en datamodell for tabellen med innhold:
	private ObservableList<Kunde> data = FXCollections.observableArrayList();
	TextField nyttKnr, nyttFnavn, nyttEnavn, nyadresse, nyttPnr, nyttKjønn;
	@Override
	public void start(Stage vindu) {
		try {
			kontroll.lagForbindelse();
			BorderPane rotpanel = new BorderPane();
			Scene scene = new Scene(rotpanel,900,600);
			vindu.setTitle("Ansattabell");
			vindu.setWidth(900);
			vindu.setHeight(600);
			TableColumn kundenr = new TableColumn("Kundenr:");
			kundenr.setMinWidth(10);	
			kundenr.setCellValueFactory(new PropertyValueFactory<Kunde, String>("kundenr"));
			TableColumn fornavn = new TableColumn("Fornavn:");
			fornavn.setMinWidth(150);	
			fornavn.setCellValueFactory(new PropertyValueFactory<Kunde, String>("fornavn"));
			TableColumn etternavn = new TableColumn("Etternavn");
			etternavn.setMinWidth(150);
			etternavn.setCellValueFactory(new PropertyValueFactory<Kunde, String>("etternavn"));			
			TableColumn adresse = new TableColumn("Adresse:");
			adresse.setMinWidth(150);
			adresse.setCellValueFactory(new PropertyValueFactory<Kunde, String>("adresse"));
			TableColumn postnr = new TableColumn("Postnr:");
			postnr.setMinWidth(150);	
			postnr.setCellValueFactory(new PropertyValueFactory<Kunde, String>("postnr"));
			TableColumn kjønn = new TableColumn("Kjønn:");
			kjønn.setMinWidth(10);	
			kjønn.setCellValueFactory(new PropertyValueFactory<Kunde, String>("kjønn"));
			tabell.getColumns().addAll(kundenr, fornavn, etternavn, adresse, postnr, kjønn);
			//innhold.add(rad);
			//Legger inn data i datamodellen:			
			tabell.setItems(data);
			//tabell.refresh();
			Label overskrift = new Label("Kundeliste");
			FlowPane registreringspanel = new FlowPane();
			nyttKnr = new TextField();
			nyttKnr.setPromptText("Kundenr:");
			nyttKnr.setMaxWidth(kundenr.getPrefWidth());
			nyttFnavn = new TextField();
			nyttFnavn.setPromptText("Navn: ");
			nyttFnavn.setMaxWidth(fornavn.getPrefWidth());
			nyttEnavn = new TextField();
			nyttEnavn.setPromptText("Etternavn: ");
			nyttEnavn.setMaxWidth(etternavn.getPrefWidth());
			nyadresse = new TextField();
			nyadresse.setPromptText("Adresse: ");
			nyadresse.setMaxWidth(adresse.getPrefWidth());
			nyttPnr = new TextField();
			nyttPnr.setPromptText("Postnr:");
			nyttPnr.setMaxWidth(postnr.getPrefWidth());
			nyttKjønn = new TextField();
			nyttKjønn.setPromptText("Kjønn");
			nyttKjønn.setMaxWidth(kjønn.getPrefWidth());
			//Oppretter en knapp:
			Button nyknapp = new Button("Legg til");
			nyknapp.setOnAction(e -> behandleNy());
			rotpanel.setTop(overskrift);
			rotpanel.setCenter(tabell);
			rotpanel.setBottom(registreringspanel);
			registreringspanel.getChildren().addAll(nyttKnr, nyttFnavn, nyttEnavn, nyadresse, nyttPnr, nyttKjønn, nyknapp);
			hentKunder();
			vindu.setScene(scene);
			vindu.show();
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public void behandleNy() {
		try {
			kontroll.oppdaterKunde(nyttKnr.getText(), nyttFnavn.getText(), nyttEnavn.getText(), nyadresse.getText(), nyttPnr.getText(), nyttKjønn.getText());
			hentKunder();
		}catch(Exception e) {System.out.println(e.getMessage());}
		nyttKnr.clear();
		nyttFnavn.clear();
		nyttEnavn.clear();
		nyadresse.clear();	
		nyttPnr.clear();
		nyttKjønn.clear();
	}
	
	public void hentKunder() {
		data.clear();
		try {
			ResultSet resultat = kontroll.lesKunder();
			while(resultat.next()) {
				ObservableList rad = FXCollections.observableArrayList();
				int kundenr = resultat.getInt(1);//I ResultSet starter indeksene på 1
				String fnavn = resultat.getString(2);
				String enavn = resultat.getString(3);
				String adr = resultat.getString(4);
				String postnr = resultat.getString(5);
				String kjønn = resultat.getString(6);
				data.add(new Kunde(kundenr, fnavn, enavn, adr, postnr, kjønn));
			}
		}catch(Exception e) {System.out.println(e.getMessage());}
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}
