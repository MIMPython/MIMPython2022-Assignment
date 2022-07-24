
def multiply(*nums) :
    mul = 1
    if len(nums) == 0 :
        return 0
    elif len(nums) == 1 :
        mul = nums[0] * nums[0]
    else :        
        for i in nums:
            mul = mul * i
    return mul

print(multiply(2,3,5,1,3,2))    #180
print(multiply(2,2))            #4
print(multiply(6))              #36
print(multiply())               #0
