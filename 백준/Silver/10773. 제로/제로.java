import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        Stack<Integer> st = new Stack<>();
        long ans = 0;
        for(int i=0; i<n; i++){
            int m = Integer.parseInt(sc.nextLine());
            if(m==0){
                if(!st.empty())st.pop();
            }else{
                st.push(m);
            }
        }
        while (!st.empty()) {
            ans += st.pop();
        }
        System.out.println(ans);
    }
}
