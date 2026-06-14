
    class Student{
        private int rollno;
        private String name;
    
        public Student(){
            rollno = 0;
            name = "empty";
        }
        public Student(int r , String n){
            rollno = r;
            name = n;
        }
        public Student(Student s){
            name = s.name;
            rollno = s.rollno;
        }
    
        public void setName(String n){
            name = n;
        }
        public void setRollno(int r){
            rollno = r;
        }
    
        public String getName(){
            return name;
        }
        public int getRollno(){
            return rollno;
        }
    
        public void print(){
            System.out.println("The name of the Student as " + getName());
            System.out.println("The Rollno of the Student as " + getRollno());
        }
    }
