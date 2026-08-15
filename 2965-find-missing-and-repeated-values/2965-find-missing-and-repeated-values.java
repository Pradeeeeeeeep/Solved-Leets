class Solution {
    public int[] findMissingAndRepeatedValues(int[][] grid) {
        int n = grid.length;
        int[] arr = new int[n * n];

        int k = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                arr[k++] = grid[i][j];
            }
        }

        Arrays.sort(arr);

        int repeated = -1;
        int missing = -1;

        for (int i = 1; i < arr.length; i++) {
            if (arr[i] == arr[i - 1]) {
                repeated = arr[i];
                break;
            }
        }

        int expected = 1;

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == expected) {
                expected++;
            }
        }

        missing = expected;

        return new int[]{repeated, missing};
    }
}