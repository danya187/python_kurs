import random
my_list = [random.randrange(1, 50, 1) for i in range(7)]

answer = []

for i in range(len(my_list)-1):
    if my_list[i] < my_list[i+1]:
        answer.append(my_list[i+1])
print(my_list)
print(answer)
