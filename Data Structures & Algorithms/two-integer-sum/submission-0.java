class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> intStore = new HashMap<>();

        for (int i = 0; i < nums.length; i ++) {
            int num = nums[i];
            int hist = target - num;

            if (intStore.containsKey(hist)) {
                return new int[] {intStore.get(hist) , i};
            }
            intStore.put(num, i);
        }
        return new int[] {};
    }
}
