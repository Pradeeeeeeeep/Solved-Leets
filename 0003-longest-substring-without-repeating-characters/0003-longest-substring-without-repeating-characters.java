class Solution {
    public int lengthOfLongestSubstring(String s) {
        boolean[] seen = new boolean[128];

        int left = 0;
        int ans = 0;

        for (int right = 0; right < s.length(); right++) {

            while (seen[s.charAt(right)]) {
                seen[s.charAt(left)] = false;
                left++;
            }

            seen[s.charAt(right)] = true;
            ans = Math.max(ans, right - left + 1);
        }

        return ans;
    }
}