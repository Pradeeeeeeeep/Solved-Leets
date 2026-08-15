class Solution {
    public int[] findMissingAndRepeatedValues(int[][] grid) {
        int n = grid.length;
        int[] freq = new int[n*n+1];
        for(int i=0; i<grid.length; i++){
            for(int j=0; j<grid[0].length; j++){
                freq[grid[i][j]]++;
            }
        }
        int repeat = -1;
        int missing = -1;
        for(int k=0; k<freq.length; k++){
            if(freq[k]==2){
                repeat = k;
            }
            if(freq[k]==0){
                missing = k;
            }
        }
        return new int[]{repeat, missing};
    }
}