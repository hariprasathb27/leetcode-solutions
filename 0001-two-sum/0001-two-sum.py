class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list_a = []
        length_of_list = len(nums)
        count=0
        while(count<length_of_list-1):
            moving_index = count+1
            while(moving_index < length_of_list):
                if(nums[count] + nums[moving_index] == target):
                    list_a.append(count)
                    list_a.append(moving_index)
                    moving_index+=1
                else:
                    moving_index+=1
            count+=1
        list_a = list(set(list_a))
        return list_a
        