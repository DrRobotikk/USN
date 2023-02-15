package applikasjon;

import javax.swing.*;

public class Grensesnitt {
    Bilregister kontroll = new Bilregister();

    public void lesFiler() {
        try {
            kontroll.lesAlleFiler();
        }catch (Exception e) {
            JOptionPane.showMessageDialog(null, e.getMessage());
        }
    }
}
