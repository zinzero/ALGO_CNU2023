n1 = int(input("작은 수 : "))
n2 = int(input("큰 수 : "))

count = 0
i = 0
for k in range(n1, n2, 1):
	for i in range(2, k + 1, 1):
		if k % i == 0:
			break	
	if k == i:
		count += 1

		if count % 5 == 0:
			print("%7d" %k)
		else:
			print("%7d" %k, end="")

print(f"\n{n1}부터 {n2}까지의 소수의 개수는 {count}개")

