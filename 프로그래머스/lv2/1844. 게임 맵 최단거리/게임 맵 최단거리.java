import java.util.Queue;
import java.util.LinkedList;

class po{
    int x;
    int y;
}

class Solution {
    static int chk[][];

    static int bfs(int[][] maps){

        Queue<po> q = new LinkedList<>();
        po tmp = new po();
        tmp.x = 0;
        tmp.y = 0;
        int dir[][] = {{1,0},{0,1},{-1,0},{0,-1}};
        chk[0][0] = 1;
        q.offer(tmp);
        int l = 1;
        while(!q.isEmpty()){
            int len = q.size();
            for(int i=0; i< len; i++){
                po n = q.poll();
                if(n.x == maps.length-1 && n.y == maps[0].length-1)return l;
                for(int j=0; j<4; j++){
                    int nx = dir[j][0]+n.x;
                    int ny = dir[j][1]+n.y;
                    if(nx>=0 && nx<maps.length && ny>=0 && ny<maps[0].length){
                        if(chk[nx][ny] == 0 && maps[nx][ny] == 1){
                            chk[nx][ny] = 1;
                            po n_tmp = new po();
                            n_tmp.x = nx;
                            n_tmp.y = ny;
                            q.offer(n_tmp);
                        }
                    }
                }
            }
            l+=1;
        }

        return -1;
    }

    public int solution(int[][] maps) {
        chk = new int[maps.length][maps[0].length];
        int answer = bfs(maps);

        return answer;
    }
}