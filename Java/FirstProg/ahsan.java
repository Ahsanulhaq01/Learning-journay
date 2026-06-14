import javax.swing.JFrame;
import javax.swing.JButton;
import java.awt.GridLayout;
class GUI{
    JFrame f;
    JButton b1,b2,b3,b4,b5,b6;

    public void init(){
        f = new JFrame("Grid layout Practice");
        b1 = new JButton("One");
        b2 = new JButton("Two");
        b3 = new JButton("Three");
        b4 = new JButton("Four");
        b5 = new JButton("Five");
        b6 = new JButton("Six");
        f.setLayout(new GridLayout(3,2,100,100));
        f.add(b1);f.add(b2);
        f.add(b3);f.add(b4);
        f.add(b5);f.add(b6);
        f.setVisible(true);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setSize(500,300);
        f.setResizable(false);
        

    }
    public GUI(){
        init();
    }
}
public class ahsan {
    public static void main(String[] args) {
        GUI g = new GUI();
    }
}
