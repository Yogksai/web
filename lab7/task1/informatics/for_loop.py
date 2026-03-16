#A
start_num = int(input())
end_num = int(input())

for n in range(start_num, end_num + 1):
    if n % 2 == 0:
        print(n, end=' ')
#B
a_start = int(input())
b_end = int(input())
c_mod = int(input())
d_div = int(input())

for num in range(a_start, b_end + 1):
    if num % d_div == c_mod:
        print(num, end=' ')
#C
start_val = int(input())
end_val = int(input())

n = 1
while n * n <= end_val:
    if n * n >= start_val:
        print(n * n, end=' ')
    n += 1
#G
num_x = int(input())

for i in range(2, num_x + 1):
    if num_x % i == 0:
        print(i)
        break
#H
num_y = int(input())

for i in range(1, num_y + 1):
    if num_y % i == 0:
        print(i, end=' ')
#I
num_z = int(input())
count_div = 0

for i in range(1, num_z + 1):
    if num_z % i == 0:
        count_div += 1

print(count_div)
#J
total_sum = 0

for _ in range(100):
    number = int(input())
    total_sum += number

print(total_sum)
#K
count_n = int(input())
sum_n = 0

for _ in range(count_n):
    num_n = int(input())
    sum_n += num_n

print(sum_n)
#M
n_total = int(input())
zero_count = 0

for _ in range(n_total):
    val = int(input())
    if val == 0:
        zero_count += 1

print(zero_count)