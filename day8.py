def summarize_pages(pages):
    if len(pages) == 0:
        return{
            "total":total,
            "fail_count":fail_count,
            "avg_score":avg_score,
            "max_score_page":max_score_page
            #极端情况会不会炸？：
            #空列表怎么办？
            # 空字符串怎么办？
            # 文件不存在怎么办？
            # API 返回空怎么办？
            # 字典里缺一个 key 怎么办？
        }

    total = 0
    fail_count = 0
    total_score = 0

    max_score = 0
    max_score_page = 0

    for page in pages:
        score = page["score"]
        page_number = page["page"]
        
        total = total + 1
        total_score = score + total_score   

        if score > 0.4:
            fail_count = fail_count + 1
        
        if score > max_score:
            max_score = score
            max_score_page = page_number

    # print("max_score:", max_score)
    # print("max_score_page:", max_score_page)
    
    # print("total:", total)
    # print("fail_count:", fail_count)
    # print("total_score:", total_score)

    avg_score = total_score / total
    # print("avg_score:",avg_score)
    result = {
        "total":total,
        "fail_count":fail_count,
        "avg_score":avg_score,
        "max_score_page":max_score_page
    }
    return result


pages = [
    {"page": 1, "score": 0.32},
    {"page": 2, "score": 0.71},
    {"page": 3, "score": 0.48},
    {"page": 4, "score": 0.21}
]
result = summarize_pages(pages)
print(result)