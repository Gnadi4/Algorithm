import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        for(int test=0; test<t; test++){
            int n = sc.nextInt();
            String s_list[] = new String[n];
            for(int i=0; i<n; i++)s_list[i] = sc.next();
            Arrays.sort(s_list);
            boolean chk = false;
            for(int i=0; i<n-1; i++){
                int j = i+1;
                if(s_list[i].length() == s_list[j].length()){
                    chk = s_list[i].equals(s_list[j]);
                }else if(s_list[i].length() < s_list[j].length()){
                    chk = s_list[i].equals(s_list[j].substring(0,s_list[i].length()));
                }else{
                    chk = s_list[j].equals(s_list[i].substring(0,s_list[j].length()));
                }
                if(chk)break;
            }
            if(chk){
                System.out.println("NO");
            }else{
                System.out.println("YES");
            }
        }
    }
}
