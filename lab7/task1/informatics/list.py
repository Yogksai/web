#A
N_arr = int(input())
arr = list(map(int, input().split()))

for i in range(0, N_arr, 2):
    print(arr[i], end=' ')
#B
N_arr2 = int(input())
arr2 = list(map(int, input().split()))

for num in arr2:
    if num % 2 == 0:
        print(num, end=' ')
#C
N_arr3 = int(input())
arr3 = list(map(int, input().split()))
count_pos = 0

for num in arr3:
    if num > 0:
        count_pos += 1

print(count_pos)
#D
N_arr4 = int(input())
arr4 = list(map(int, input().split()))
count_greater = 0

for i in range(1, N_arr4):
    if arr4[i] > arr4[i-1]:
        count_greater += 1

print(count_greater)
#E
N_arr5 = int(input())
arr5 = list(map(int, input().split()))
found = False

for i in range(1, N_arr5):
    if arr5[i] * arr5[i-1] > 0:
        found = True
        break

print("YES" if found else "NO")
#F
N_arr6 = int(input())
arr6 = list(map(int, input().split()))
count_peak = 0

for i in range(1, N_arr6 - 1):
    if arr6[i] > arr6[i-1] and arr6[i] > arr6[i+1]:
        count_peak += 1

print(count_peak)
#G
N_arr7 = int(input())
arr7 = list(map(int, input().split()))

arr7.reverse()
for num in arr7:
    print(num, end=' ')
#H
N_arr8 = int(input())
arr8 = list(map(int, input().split()))

arr8.sort(reverse=True)
for num in arr8:
    print(num, end=' ')
#I
N_arr9 = int(input())
arr9 = list(map(int, input().split()))

arr9 = arr9[1:] + arr9[:1]
for num in arr9:
    print(num, end=' ')
#J
N_arr10 = int(input())
arr10 = list(map(int, input().split()))

print(max(arr10))
#K
N_arr11 = int(input())
arr11 = list(map(int, input().split()))

print(len(set(arr11)))
#L
N_students = int(input())
heights = list(map(int, input().split()))
petya_height = int(input())

position = 1
for h in heights:
    if h >= petya_height:
        position += 1

print(position)
#M
N_seq, A, B, C, D = map(int, input().split())

result = [0] * N_seq
used = [False] * (N_seq + 1)

# place 1 to A
for i in range(1, A + 1):
    result[i - 1] = i
    used[i] = True

# place B to C
for i in range(B, C + 1):
    result[i - 1] = i
    used[i] = True

# place D to N
for i in range(D, N_seq + 1):
    result[i - 1] = i
    used[i] = True

# fill remaining numbers
idx = 0
for num in range(1, N_seq + 1):
    if not used[num]:
        while result[idx] != 0:
            idx += 1
        result[idx] = num

print(*result)