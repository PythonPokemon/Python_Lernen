nums = [1,2,3,4,5,6,7,8,9,]
nums2 = nums

print("speicheradresse von nums", id(nums))     # speicheradresse: 2574584822272
print("speicheradresse von nums2",id(nums2))    # speicheradresse: 2574584822272

vals = nums[0:5]    # speicheradresse: 2574584704960
print("speicheradresse von vals",id(vals))
