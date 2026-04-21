#Day 17 - Test
def test_args(*nums):
    return len(nums) == 3

result = test_args(1, 2, 3)
print("3 args:", result)
print("Day 17 test ok")