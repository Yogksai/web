#A
def min_of_four_nums(num1_mf, num2_mf, num3_mf, num4_mf):
    return min(num1_mf, num2_mf, num3_mf, num4_mf)

# Пример использования
a_mf, b_mf, c_mf, d_mf = map(int, input().split())
print(min_of_four_nums(a_mf, b_mf, c_mf, d_mf))
#B
def power_calc(base_pw, exp_pw):
    result_pw = 1.0
    for _ in range(exp_pw):
        result_pw *= base_pw
    return result_pw

# Пример использования
a_pw, n_pw = input().split()
a_pw = float(a_pw)
n_pw = int(n_pw)
print(power_calc(a_pw, n_pw))
#C
def xor_func(x_xor, y_xor):
    return (x_xor and not y_xor) or (not x_xor and y_xor)

# Пример использования
x_input_xor, y_input_xor = map(int, input().split())
x_bool_xor = bool(x_input_xor)
y_bool_xor = bool(y_input_xor)
print(int(xor_func(x_bool_xor, y_bool_xor)))