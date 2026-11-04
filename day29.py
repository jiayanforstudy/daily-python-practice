

# def first_unique_char(s):
#     char_count = {}
#     for char in s:
#         if char in char_count:
#             char_count[char] += 1

#         else:
#             char_count[char] = 1

# ###简洁写法：
# #for char in s:
# #    char_count[char] = char_count.get(char,0) + 1
# # get(char, 0) 的意思是：
# # - 如果字典中有这个字符，取出它的次数。
# # - 如果没有，就返回 0

#     for i, char in enumerate(s):
#         if char_count[char] == 1:
#             return i
    
#     return -1

# print(first_unique_char("leetcode"))
# print(first_unique_char("loveleetcode"))
# print(first_unique_char("aabb"))
# print(first_unique_char(""))
# print(first_unique_char("aabbc"))

def most_frequent_char(s):
    char_count = {}

    if not s:
        return None


    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    most_frequent = max(char_count, key=char_count.get)
    
    return most_frequent

print(most_frequent_char("aabbbccccddddd"))  # d
print(most_frequent_char("banana"))          # a
print(most_frequent_char("xxxx"))            # x
print(most_frequent_char(""))                # None

