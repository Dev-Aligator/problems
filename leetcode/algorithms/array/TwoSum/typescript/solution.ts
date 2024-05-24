function twoSum(nums: number[], target: number): number[] {
  // Create an array of objects with value and original index
  let numsWithIndex = nums.map((value, index) => ({ value, index }));
  
  // Sort the array based on the values
  numsWithIndex.sort((a, b) => a.value - b.value);
  
  let l = 0, r = numsWithIndex.length - 1;
  while (r > l) {
    const val = numsWithIndex[l].value + numsWithIndex[r].value;
    if (val == target) {
      return [numsWithIndex[l].index, numsWithIndex[r].index];
    } else if (val > target) {
      r -= 1;
    } else {
      l += 1;
    }
  }

  // If no solution is found, return an empty array (though the problem guarantees one solution)
  return [];
}

console.log(twoSum([2, 11, 7, 15], 9)); // Output: [0, 2]
