import java.util.HashMap;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        
        HashMap<Integer, Integer> h  = new HashMap<>();
        
        for(int i: nums){
            h.put(i, 1);
        }
        
        return Math.min(nums.length/2, h.size());
    }
}