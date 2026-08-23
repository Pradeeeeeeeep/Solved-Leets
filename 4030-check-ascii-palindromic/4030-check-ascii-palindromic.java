class Solution {
    public boolean isPalindromic(String s) {
        StringBuilder ans = new StringBuilder();

        for (char c : s.toCharArray()) {
            ans.append(toBinary(c));
        }

        for (int i = 0, j = ans.length() - 1; i < j; i++, j--) {
            if (ans.charAt(i) != ans.charAt(j)) {
                return false;
            }
        }

        return true;
    }

    static String toBinary(char c) {
        int n = c;
        StringBuilder s = new StringBuilder();

        while (n > 0) {
            s.append(n % 2);
            n /= 2;
        }

        while (s.length() < 8) {
            s.append('0');
        }

        return s.reverse().toString();
    }
}