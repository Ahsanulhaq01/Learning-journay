package Prog3;

import javax.swing.*;
import java.awt.*;
class GUI{
    JFrame frame;
    JPanel textpanal,buttonpanal;
    JButton first,pre,next,last,exit,add,delete,edit,cancel,save;
    JLabel stdId,stdName,stdAddress;
    JTextArea id,name,address;
    public void init(){
        JFrame frame = new JFrame("Student data form ");
        JPanel textpanal = new JPanel();
        JPanel buttonpanal = new JPanel();
        JButton first = new JButton("First");JButton pre = new JButton("Previous");JButton next = new JButton("Next");JButton last = new JButton("Last");JButton exit = new JButton("Exit");JButton add = new JButton("Add");JButton delete = new JButton("Delete");JButton edit = new JButton("Edit");JButton cancel = new JButton("Cancel");JButton save = new JButton("Save");

        JLabel stdId = new JLabel("Student ID : ");
        JLabel stdName = new JLabel("Student Name : ");
        JLabel stdAddress = new JLabel("Student Address");
        JTextArea id = new JTextArea();
        JTextArea name = new JTextArea();
        JTextArea address = new JTextArea();

        textpanal.setLayout(new GridLayout(3,2,10,30));
        buttonpanal.setLayout(new GridLayout(2,5,10,30));
    

        textpanal.add(stdId);
        textpanal.add(id);
        textpanal.add(stdName);
        textpanal.add(name);
        textpanal.add(stdAddress);
        textpanal.add(address);

        buttonpanal.add(first);
        buttonpanal.add(pre);
        buttonpanal.add(next);
        buttonpanal.add(last);
        buttonpanal.add(exit);
        buttonpanal.add(add);
        buttonpanal.add(delete);
        buttonpanal.add(edit);
        buttonpanal.add(cancel);
        buttonpanal.add(save);

        frame.add(textpanal,BorderLayout.NORTH);
        frame.add(buttonpanal,BorderLayout.SOUTH);

        frame.setVisible(true);
        frame.setSize(500,300);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        Container c = frame.getContentPane();
        c.setBackground(Color.RED);
        textpanal.setBackground(Color.red);
        buttonpanal.setBackground(Color.red);

        stdId.setForeground(Color.white);
        stdName.setForeground(Color.white);
        stdAddress.setForeground(Color.white);

        first.setBackground(Color.black);
        first.setForeground(Color.white);
    }
    public GUI(){
        init();
    }
}
public class ProgramGui {
    public static void main(String[] args) {
        GUI g = new GUI();
    }
}
