function containsDuplicate(nums: number[]): boolean {
  let stored:number[] = []

  for (var value of nums) {
    if(stored[value])
    return true
    stored[value] = 1
  }
  return false


};

console.log(containsDuplicate([1,2,3,1]))
