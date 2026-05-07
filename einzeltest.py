nums = []
vals = nums[:]
vals.append(1)

print(nums)
print(vals)
print(id(nums))
print(id(vals))

print(nums is vals)
print(nums == vals)