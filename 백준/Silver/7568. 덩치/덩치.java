import java.util.Scanner;

public class Main {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        int list_n[][] = new int[n][2];

        for(int i=0; i<n; i++){
            String s[] = sc.nextLine().split(" ");
            list_n[i][0] = Integer.parseInt(s[0]);
            list_n[i][1] = Integer.parseInt(s[1]);
        }
        int ans[] = new int[n];
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if(list_n[i][0]<list_n[j][0] && list_n[i][1]<list_n[j][1])ans[i]+=1;
            }
        }
        for(int i: ans){
            System.out.print(i+1+" ");
        }
        System.out.println();
    }
}
