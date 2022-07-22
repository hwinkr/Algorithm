import java.util.ArrayList;
import java.util.Scanner;

public class FIndSt {
    static Scanner sc = new Scanner(System.in);
    static Student st[] = new Student[3];
    public static void main (String[] args){
        String stName[] = {"최","박","김"};
        int stNumber[] = {201912,201917,201911};
        for (int i=0; i<st.length; i++) st[i] = new Student(stName[i],stNumber[i]);
        ArrayList <Student> list = new ArrayList<Student>();
        for (int i =0; i<st.length; i++) list.add(st[i]);
        while (true){
            System.out.println("Do you Want Find? (y/n) : ");
            String answer = sc.next();
            if(answer.equals("y")){
                System.out.print("enter Student Name who you want to find : ");
                String name = sc.next();
                boolean flag = false;
                for (Student student : list){
                    if (student.name.equals(name)) student.getNumber();
                }
                // if flag is false.
                if (!flag){
                   System.out.println("There isn't Student who you want to find.");
                }
            }
            else if (answer.equals("n")){
                break;
            }
        }
        System.out.println("program is end.");
        System.out.println("Good Bye!");
    }
}
class Student{
    String name;
    int number;
    Student(String name , int number){
        this.name = name;
        this.number =number;
    }
    void getName() {
        System.out.println(this.name);
    }
    void getNumber() {
        System.out.println(this.number);
    }
}
class Student1{
    String name;
    int number;
    Student1(String name , int number){
        this.name = name;
        this.number =number;
    }
    void getName() {
        System.out.println(this.name);
    }
    void getNumber() {
        System.out.println(this.number);
    }
}
