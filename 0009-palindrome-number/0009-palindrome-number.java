class Solution {
    public boolean isPalindrome(int x) {
        int num = x;
        int pnum = 0;
        if(num<0){
            return false;
        }
        while(num>0) {
            int d = num%10;
            pnum = pnum*10+d;
            num = num/10;
        }
        if (pnum == x){
            return true;
        } else {
            return false;
        }
    }
}