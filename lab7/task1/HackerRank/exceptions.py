for _ in range(int(input())):
    a_str, b_str = input().split()
    try:
        a_int = int(a_str)
        b_int = int(b_str)
        print(a_int // b_int)
    except (ZeroDivisionError, ValueError) as e:
        print("Error Code:", e)