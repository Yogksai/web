#A
N_limit = int(input())
n = 1

while n * n <= N_limit:
    print(n * n)
    n += 1
#B
N_val = int(input())
count_divisors = 0

for i in range(2, N_val + 1):
    if N_val % i == 0:
        count_divisors += 1

print(count_divisors)
#C
N_max = int(input())
power = 1

while power <= N_max:
    print(power, end=' ')
    power *= 2
#D
num_check = int(input())

n = 1
is_power_of_two = False

while 2 ** n <= num_check:
    if 2 ** n == num_check or num_check == 1:
        is_power_of_two = True
        break
    n += 1

print("YES" if is_power_of_two else "NO")
#E
N_input = int(input())
count = 0
i = 1

while i * i <= N_input:
    count += 1
    i += 1

print(count)