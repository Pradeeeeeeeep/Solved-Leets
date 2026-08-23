class Solution {
    public int trap(int[] height) {
        int n = height.length;
        int ans = 0;
        int[] lmax = new int [n];
        int[] rmax = new int [n];
        lmax[0] = height[0];
        rmax[n-1] = height[n-1];
        for(int i=1; i<n; i++){
            lmax[i]=Math.max(lmax[i-1], height[i]);
        }
        for(int j=n-2; j>=0; j--){
            rmax[j]=Math.max(rmax[j+1], height[j]);
        }
        for(int k=0; k<n; k++){
            ans+=Math.min(lmax[k], rmax[k])-height[k];
        }
        return ans;
    }
}