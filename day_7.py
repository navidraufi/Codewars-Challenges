# def permute(s):
#     if len(s) == 1:
#         return [s]
#     else:
#         perms = set()
#         for i in range(len(s)):
#             first_char = s[i]
#             remaining_chars = s[:i] + s[i+1:]
#             for perm in permute(remaining_chars):
#                 perms.add(first_char + perm)
#         return list(perms)


# import itertools

# # def permutations(string):
# #     return list("".join(p) for p in set(itertools.permutations(string)))



# # def permutations(string):
# #     return ["".join(i) for i in set(itertools.permutations(string))]

# print(permutations("aabb"))


# def solution(s):
#     final_array = []
#     if len(s) % 2:
#         s += "_"
#     for i in range(0, len(s),2):
#         final_array.append(s[i:i+2])
    
#     return final_array

# print(solution("alsmdn"))

# def boolean_to_string(b):
#     return 'True' if b else 'False'




# def positive_sum(arr):
#     sum = 0
#     for i in arr:
#         if i > 0:
#             sum+=i
    
#     return sum


# def positive_sum(arr):
#     return sum(i for i in arr if i > 0)


# print(positive_sum([1,2,6]))

# def filter_list(l):
#     return [i for i in l if type(i) == int]
    
# print(filter_list([1, 2, "aasf", "1", "123", 123]))



# return masked string
# def maskify(cc):
#     # final_ans = []
#     # for i in range(len(cc)):
#     #     final_ans.append(cc[])

#     return (len(cc) - 4) * "#"  + cc[len(cc) - 4 :] if len(cc) > 4 else cc

# print(maskify("12334"))

# def maskify(cc):
#     return "#"*(len(cc)-4) + cc[-4:]