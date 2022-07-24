class Solution {    
    static int ans = 0;
    
    public void dfs(int numbers[], int target, int n){
        if(n == numbers.length){
            if(target == 0){
                ans += 1;
            }
        }else{
            dfs(numbers, target-numbers[n], n+1);
            dfs(numbers, target+numbers[n], n+1);
        }
    }
    
    public int solution(int[] numbers, int target) {
        dfs(numbers, target, 0);
        return ans;
    }
}