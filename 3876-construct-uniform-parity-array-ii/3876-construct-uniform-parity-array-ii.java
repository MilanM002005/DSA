class Solution {
    public boolean uniformArray(int[] a) {
        int mn = Integer.MAX_VALUE;
        int odd = 0;
        for (int x : a) {
            mn = Math.min(mn, x);
            if (x % 2 == 1) odd++;
        }
        return mn % 2 != 0 || odd == 0;
    }
}