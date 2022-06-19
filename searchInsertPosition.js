
 var searchInsert = function(nums, target) {
    nums.push(target);
    for(let i =0; i< nums.length; i++){
        for(let j =0; j<nums.length-1; j++){
            if(nums[j] > nums[j+1]){
                let temp = nums[j];
                nums[j] = nums[j+1];
                nums[j+1] = temp;
            }
        }
    }

    for(let i = 0; i < nums.length; i++){
        if(nums[i] === target){
            return i;
        }
    }
    
};