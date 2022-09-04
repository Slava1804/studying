# def digital_root(n):
#     n = str(n)
#     mass_numbers = [int(n[i]) for i in range(len(n))]
#     res = 0
#     while len(mass_numbers) != 0:
#         res += mass_numbers[-1]
#         del mass_numbers[-1]
#         if res // 10 != 0:
#             mass_numbers = [int(res[j]) for j in range(len(str(res)))]
#         else:
#             return res

# num = int(input())
# print(digital_root(num))
# n = 0 // 10
# print(n)