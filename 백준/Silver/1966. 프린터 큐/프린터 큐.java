import java.util.*;

public class Main {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int test = Integer.parseInt(sc.nextLine());
        for(int t=0; t<test; t++){
            String tmp[] = sc.nextLine().split(" ");
            int n=Integer.parseInt(tmp[0]), m=Integer.parseInt(tmp[1]);
            Queue<arr> q = new LinkedList<arr>();
            String tmp2[] = sc.nextLine().split(" ");
            Integer sarr[] = new Integer[n];
            for(int i=0; i<n; i++) {
                arr tmp_arr = new arr();
                tmp_arr.val = Integer.parseInt(tmp2[i]);
                tmp_arr.ind = i;
                sarr[i] = tmp_arr.val;
                q.add(tmp_arr);
            }
            Arrays.sort(sarr, Collections.reverseOrder());
            Queue<Integer> q_sarr = new LinkedList<Integer>();
            for(int i: sarr){
                q_sarr.add(i);
            }

            int ans = 1;
            while(!q.isEmpty()){
                arr a = q.poll();
                if(a.val == q_sarr.peek()){
                    q_sarr.remove();
                    if(a.ind == m){
                        System.out.println(ans);
                        break;
                    }
                    ans += 1;
                }else{
                    q.add(a);
                }
            }
        }
    }
}

class arr{
    int val;
    int ind;
}