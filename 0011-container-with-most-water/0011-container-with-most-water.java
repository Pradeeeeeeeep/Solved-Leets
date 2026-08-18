class Solution {
    public int maxArea(int[] height) {
        int area = 0;
        int l=0;
        int r=height.length-1;
        while(l<r){
            int w = r-l;
            int h = Math.min(height[l], height[r]);
            int temp = w*h;
            area = Math.max(area, temp);
            if(height[l]<height[r]) l++; else r--; 
        }
        return area;
    }
}