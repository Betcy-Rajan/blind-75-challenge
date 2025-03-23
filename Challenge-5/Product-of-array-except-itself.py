nums=list(map(int,input().split()))
# def productExceptSelf(nums):
#         n=len(nums)
#         answer=[1]*n
#         for i in range(0,len(nums)):
#             product=1
#             for j in range(len(nums)-1,-1,-1):
#                 if i==j:
#                     continue
#                 product*=nums[j]
#             answer[i]=product
#         return answer
# print(productExceptSelf(nums))
# #TC is O(n^2) and SC is O(n)

def productExceptSelf(nums):
        n=len(nums)
        ans=[0]*n
        left=1
        right=1
        for i,val in enumerate(nums):
                ans[i]=left
                left*=val #val = nums[i]
        for i in range(n-1,-1,-1):
                ans[i]*=right
                right*=nums[i]
        return ans
print(productExceptSelf(nums))
#TC is O(n) and SC is O(1)
#i	nums[i]	left (before update)	ans[i] (stores left)	left (after update)
# 0	    1	    1	                    1	                1 × 1 = 1
# 1	    2	    1	                    1	                1 × 2 = 2
# 2	    3	    2	                    2	                2 × 3 = 6
# 3	    4	    6	                    6	                6 × 4 = 24

#i	nums[i]	right (before update)	ans[i] (stores right)	right (after update)
# 3   4        1	                    6 x1 =6	                1 × 4 = 4
# 2   3        4	                    2 x 4 =8	            4 × 3 = 12
# 1   2        12	                    1 x 12 =12	            12 × 2 = 24
# 0   1        24	                    1 x 24 =24	            24 × 1 = 24


#ans=[24,12,8,6]