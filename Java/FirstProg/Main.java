import javax.swing.JFrame;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.FlowLayout;
class GUI{
    JFrame f;
    JButton button;
    JTextArea text ;

    public void  init(){
        f = new JFrame("First User Interface Program");
        button = new JButton("Cancel the program");
        text = new JTextArea("I am ahsanulhaq");
        f.add(button);
        f.add(text);
        f.setSize(500,300);
        f.setVisible(true);
        f.setLayout(new FlowLayout());
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
    }
    public GUI(){
        init();
    }


}
public class Main {
public static void main(String[] args) {
   GUI g = new GUI();

}
    
}