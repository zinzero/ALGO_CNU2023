num_lst = list(map(int, input("리스트 입력 : ").split()))

max_value = 0

for i in num_lst:
	if i > max_value:
		max_value = i

print("입력된 리스트 : ", num_lst)
print("최댓값 : ", max_value)

