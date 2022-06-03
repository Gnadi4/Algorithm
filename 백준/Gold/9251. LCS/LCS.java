import java.util.Scanner;

public class Main {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        char c1[] = sc.next().toCharArray();
        char c2[] = sc.next().toCharArray();

        int ans[][] = new int[c2.length][c1.length];

        for(int i=0; i<c2.length; i++){
            int inp = 0;
            for(int j=0; j<c1.length; j++){
                if(i==0){
                    if(c1[j] == c2[i])inp = 1;
                    ans[i][j] = inp;
                }else{
                    if(j==0){
                        if(c1[j] == c2[i])ans[i][j] = 1;
                        else{ans[i][j]=ans[i-1][j];}
                    }else{
                        if(c1[j]==c2[i]){
                            ans[i][j] = Math.max(ans[i-1][j], ans[i-1][j-1]+1);
                        }else{
                            ans[i][j] = Math.max(ans[i-1][j], ans[i][j-1]);
                        }
                    }
                }
            }
        }

//        for(int i=0; i<c2.length; i++){
//            for(int j=0; j<c1.length; j++){
//                System.out.print(ans[i][j]+" ");
//            }
//            System.out.println();
//        }

        System.out.println(ans[c2.length-1][c1.length-1]);
    }
}
