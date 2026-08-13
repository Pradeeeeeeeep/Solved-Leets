class Solution {
    public boolean isPerfectSquare(int num) {
        int top = num/2;
        if(num == 1) {
            return true;
        }
        for(int i = 0; i <= top; i++){
            if(i*i == num){
                return true;
            }
        }
        return false;
    }
}