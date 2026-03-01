n = int(input("Enter a number: "))
sum = 0
even = 0
for i in range(1,n+1):
    sum += i
    if i %2 == 0:
        even += 1
print("Summ:", sum)
print("Even numbers:", even)
