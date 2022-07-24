import java.util.LinkedList;
import java.util.Queue;

class Solution {
    static int chk[];
    static int bfs(String begin, String target, String[] words){
        boolean chk_tmp = false;
        for(String s: words){
            if(s.equals(target))chk_tmp = true;
        }
        if(!chk_tmp)return 0;
        
        Queue<String> q = new LinkedList<>();
        q.add(begin);
        int l = 0;
        
        while(!q.isEmpty()){
            int len = q.size();
            for(int i=0; i<len; i++){
                String s = q.poll();
                if(s.equals(target))return l;
                for(int j=0; j<words.length; j++){
                    char c1[] = s.toCharArray();
                    char c2[] = words[j].toCharArray();
                    int dif = 0;
                    for(int k=0; k<words[j].length(); k++){
                        if(c1[k]!=c2[k])dif+=1;
                    }
                    if(dif == 1 && chk[j] == 0){
                        chk[j] = 1;
                        q.offer(words[j]);
                    }
                }
            }
            l+=1;
        }
        return 0;
    }
    
    public int solution(String begin, String target, String[] words) {
        chk = new int[words.length];
        int answer = bfs(begin, target, words);
        return answer;
    }
}