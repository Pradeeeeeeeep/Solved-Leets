class Solution {
    public int[] runningSum(int[] nums) {
        int[] cNum = nums.clone();
        for(int i=1; i<nums.length; i++){
            int tempSum = 0;
            for(int j=0; j<i; j++){
                tempSum += cNum[j];
            }
            nums[i] += tempSum;
        }
        return nums;
    }
}