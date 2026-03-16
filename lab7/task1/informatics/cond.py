#A
num_a = int(input())
num_b = int(input())
print(max(num_a, num_b))
#B
year_val = int(input())
if (year_val % 4 == 0 and year_val % 100 != 0) or (year_val % 400 == 0):
    print("YES")
else:
    print("NO")
#C
system_answer = int(input())
student_answer = int(input())

if system_answer == 1 and student_answer != 1:
    print("YES")
elif system_answer != 1 and student_answer == 1:
    print("YES")
elif system_answer == student_answer:
    print("YES")
else:
    print("NO")
#D
x_val = int(input())
if x_val > 0:
    print(1)
elif x_val < 0:
    print(-1)
else:
    print(0)
#E
val1 = int(input())
val2 = int(input())

if val1 > val2:
    print(1)
elif val2 > val1:
    print(2)
else:
    print(0)