package application;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class Kontroll {
	private String databasenavn = "jdbc:mysql://localhost:3306/hobbyhuset";
    private String databasedriver = "com.mysql.jdbc.Driver";
    private Connection forbindelse;
    private ResultSet resultat;
    private Statement utsagn;
    
    public void lagForbindelse() throws Exception {        
	try {
            forbindelse = DriverManager.getConnection(databasenavn,"root","passord");
		} catch(Exception e) {                    
            throw new Exception("Kan ikke oppnå kontakt med databasen");                        
		}            
    }
    
    public void lukk() throws Exception {
        try {
            if(forbindelse != null) {
                forbindelse.close();
                //resultat.close();
                //utsagn.close();
            }
        }catch(Exception e) {
            throw new Exception("Kan ikke lukke databaseforbindelse");
        }        
    }
    
    public ResultSet lesKunder() throws Exception {
    	ResultSet resultat = null;
    	String sql = "SELECT * FROM Kunde";
    	try {
    		utsagn = forbindelse.createStatement();
    		resultat = utsagn.executeQuery(sql);
    	}catch(Exception e) {throw new Exception("Kan ikke åpne databasetabell");}
    	return resultat;
    }
    
    public void oppdaterKunde(String knr, String fnavn, String enavn, String adresse, String pnr, String kjønn) throws Exception {
    	int kundenr = Integer.parseInt(knr);
    	String sqlsetning = "INSERT INTO hobbyhuset.kunde VALUES(" + kundenr + ",'" + fnavn + "','" 
    			+ enavn + "','" + adresse + "','" + pnr + "','" + kjønn + "');";
    	System.out.println(sqlsetning);
    	try {
    		Statement utsagn = forbindelse.createStatement();
    		utsagn.executeUpdate(sqlsetning); 
    	}catch(Exception e) {throw new Exception("Kan ikke lagre data");}
    }    

}
