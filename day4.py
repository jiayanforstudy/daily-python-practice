
# def quality_check(score) :
#     if score > 0.4 :
#         return "FALL"
#     else:
#         return "PASS"

# result1 = quality_check(0.35)
# result2 = quality_check(0.5)

# print(result1)
# print(result2)

def quality_check(score,threshold) :
    if score > threshold :
        return "FALL"
    else:
        return "PASS"


print(quality_check(0.35,0.4))
print(quality_check(0.5,0.4))
print(quality_check(0.55,0.6))
