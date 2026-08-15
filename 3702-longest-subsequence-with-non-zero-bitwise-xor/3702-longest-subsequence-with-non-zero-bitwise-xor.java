class Solution {
    public int longestSubsequence(int[] nums) {
        int xorValue = 0;

        for (int x : nums)
            xorValue ^= x;

        if (xorValue != 0)
            return nums.length;

        for (int x : nums)
            if (x != 0)
                return nums.length - 1;

        return 0;
    }
}