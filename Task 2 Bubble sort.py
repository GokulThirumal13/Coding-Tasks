def bubble_sort(nums):
    n=len(nums)
    for i in range(n):
        for j in range(0,n-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums

nums=list(map(int,input().split()))
result=bubble_sort(nums)
print(result)