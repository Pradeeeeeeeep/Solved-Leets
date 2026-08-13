class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int greatestNum = Integer.MIN_VALUE;
        List<Boolean> ans = new ArrayList<>();
        for(int num : candies){
            if(num>greatestNum){
                greatestNum = num;
            }
        }
        for(int i=0; i<candies.length; i++){
            if((candies[i]+extraCandies) >= greatestNum){
                ans.add(true);
            } else {
                ans.add(false);
            }
        }
        return ans;
    }
}