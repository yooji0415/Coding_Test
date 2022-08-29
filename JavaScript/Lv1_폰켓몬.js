function solution(nums) {
  const numSet = new Set(nums);
  return Math.min(numSet.size, parseInt(nums.length / 2));
}
