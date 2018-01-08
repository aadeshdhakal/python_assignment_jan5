nums = []
for each in range(0,101):
    nums.append(each)
prime = []
fp = open("prime.txt", "w")

for each in nums:
    for i in range(2, each - 1):
        if each%i == 0:
            break
    else:
        prime.append(each)

fp.write(str(prime))
fp.close()

