import json

def analyze_document(pages):
    total_pages = len(pages)

    total_score = 0
    fail_pages = 0
    max_score = 0
    best_page = None
    if not pages:
        return  {
                "total_score": 0,
                "fail_pages": 0,
                "best_page": 0,
                "avg_score": None
                
            }
    for page in pages:
        

        score = page["score"]

        total_score = total_score + score
        if score < 0.4:
            fail_pages = fail_pages + 1
        if score > max_score:
            max_score = score
            best_page = page["page"]

    avg_score = total_score / total_pages

    result = {
        "total_score": total_score,
        "fail_pages": fail_pages,
        "best_page": best_page,
        "avg_score": avg_score
        
    }
    return result

with open("sample copy.json","r",encoding="utf-8") as f:
    pages = json.load(f)

result = analyze_document(pages)
print(result)

with open("result copy.json","w",encoding="utf-8") as f :
    json.dump(result,f,ensure_ascii=False,indent=4)
