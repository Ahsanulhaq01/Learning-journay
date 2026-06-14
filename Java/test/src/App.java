public class App {
    public static void main(String[] args) throws Exception {
      Student s1 = new Student();
      s1.print();
      Student s2  = new Student(4,"ahsan");
      s2.print();
      Student s3 = new Student(s1);
      s3.print();
      Student s4 = new Student(s2);
      s4.print();
    }
}


