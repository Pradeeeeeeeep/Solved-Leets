class Solution {
    public int maximumWealth(int[][] accounts) {
        int ans = 0;
        for(int row=0; row<accounts.length; row++){
            int tempSum = 0;
            for(int col=0; col<accounts[row].length; col++){
                tempSum += accounts[row][col];
            }
            if(tempSum>ans){
                ans = tempSum;
            }
        }
        return ans;
    }
}