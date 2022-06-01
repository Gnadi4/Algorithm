import java.util.Scanner;

public class Main {

    public static void main(String args[]){
        Scanner in = new Scanner(System.in);

        while(true){
            String s = in.nextLine();
            if(s.equals("0"))break;
            String s_new[] = s.split(" ");
            String s_tmp[] = new String[Integer.parseInt(s_new[0])];
            for(int i=0; i<Integer.parseInt(s_new[0]); i++){
                s_tmp[i] = s_new[i+1];
            }
            String ans[] = new String[6];
            func(0, s_tmp, ans, 0);
            System.out.println();
        }

    }

    static void func(int st, String s[], String ans[], int chk){
        if(chk==6){
            for(String i:ans) {
                System.out.print(i+' ');
            }System.out.println();
        }else if(chk < 6){
            for(int i=st; i<s.length; i++){
                ans[chk] = s[i];
                func(i+1, s, ans, chk+1);
            }
        }
        return;
    }
}