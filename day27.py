nums = [2,7,11,15]


#两个循环的方法：

# def two_sum(nums,target):
#     for i in range(len(nums)):
#         for j in range(i + 1,len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i,j]

#用字典把两个循环优化成一个循环：

def two_sum(nums,target):
    seen = {}
    for i in range(len(nums)):
        num = nums[i]
        need = target - num
        if need in seen:
            return [seen[need],i]
        seen[num] = i




result = two_sum(nums,9)
print(result)
print(two_sum([2,7,11,15],9))
print(two_sum([3,2,4],6))
print(two_sum([3,3],6))
