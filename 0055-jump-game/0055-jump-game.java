class Solution {
    public boolean canJump(int[] nums) {
        int curMax = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (curMax < i) return false; 
            curMax = Math.max(curMax, i + nums[i]);
        }
        return true;  
    }
}