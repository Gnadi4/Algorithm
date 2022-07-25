class Solution {
    static int chk[];
    static String ans = "";
    
    static void dfs(String s, String tickets[][], String tmp){
        if(tmp.length() == 3*tickets.length+3){
            if(ans.equals("")){
                ans = tmp;
                return;
            }else if(ans.compareTo(tmp)>0){
                ans = tmp;
                return;
            }
        }
        for(int i=0; i<tickets.length; i++){
            if(chk[i] == 0 && tickets[i][0].equals(s)){
                chk[i] = 1;
                dfs(tickets[i][1], tickets, tmp+tickets[i][1]);
                chk[i] = 0;
            }
        }
        return;
    }
    
    public String[] solution(String[][] tickets) {
        String[] answer = {};
        chk = new int[tickets.length];
        dfs("ICN", tickets, "ICN");
        String tmp = ans;
        answer = new String[tickets.length+1];
        int ind = 0;
        char arr[] = tmp.toCharArray();
        String in = "";
        for(int i=0; i<arr.length; i++){
            in += arr[i];
            if(i%3==2){
                answer[i/3] = in;
                in = "";
            }
        }
        return answer;
    }
}