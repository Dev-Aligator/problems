function search(nums: number[], target: number): number {
  let left = 0, right = nums.length -1, mid:number

  while (left <= right) {
    mid = Math.floor((left + right) / 2)

    if (nums[mid] == target){
      return mid;
    }

    else if (nums[mid] < target) {
      left = mid + 1
    }
    else {
      right = mid - 1
    }
  }
  return -1
};

console.log(search([-1,0,3,5,9,12], 9))
