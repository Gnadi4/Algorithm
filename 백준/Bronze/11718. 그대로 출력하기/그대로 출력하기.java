import java.util.Scanner;

public class Main {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        while(sc.hasNextLine()){
            String ans = sc.nextLine();
            if(ans.isEmpty())break;
            else{System.out.println(ans);}
        }
    }
}
