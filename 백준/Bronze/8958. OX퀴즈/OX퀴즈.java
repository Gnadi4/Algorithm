import java.util.Scanner;

public class Main {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for(int test = 0; test<n; test++) {
            int ans = 0;
            char s_list[] = sc.next().toCharArray();
            int pos = 1;
            for(char i:s_list){
                if(i=='O'){
                    ans += pos;
                    pos += 1;
                }else{
                    pos = 1;
                }
            }
            System.out.println(ans);
        }
    }
}
