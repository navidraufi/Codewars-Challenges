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


def solution(s):
    final_array = []
    
    if len(s) % 2:
        s += "_"
        # 
    for i in range(0, len(s),2):
        final_array.append(s[i:i+2])
    
    return final_array

print(solution("alsmdn"))