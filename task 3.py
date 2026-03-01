import random
nums = []
for i in range(10):
    nums.append(random.randint(1, 100))
max1 = 0
for i in range(10):
    if nums[i] > max1:
        max1 = nums[i]
min1 = nums[0]
for i in range(1,10):
    if nums[i] < min1:
        min1 = nums[i]
sum1 = 0

even = []
for i in range(10):
    sum1 += nums[i]
    if nums[i] % 2 == 0:
        even.append(nums[i])
ave = sum1 / 10
print("Список чисел:", nums)
print("Максимальное число:", max1)
print("Минимальное число:", min1)
print("Список только чётных чисел:", even)
print("Среднее значение:", ave)

