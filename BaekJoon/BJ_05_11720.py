# sum 함수를 이용
n = input()

print(sum(map(int,input())))

# for 문을 이용 - 1
n = input()
nums = input()
total = 0
for i in nums :
    total += int(i)  # total= total+int(i)
print(total)

# for 문을 이용 - 2
n = input()
nums = input()
total = 0
for i in range(n) :  # 0부터 n-1까지
    total += int(nums[i])
print(total)