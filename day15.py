import json

def load_pages(filename):
    try:
        with open(filename,"r",encoding="utf-8") as f:
            pages = json.load(f)

        return pages
    except FileNotFoundError:
        print("File not found")
        return []
    except json.JSONDecodeError:
        print("Invalid JSON format")
        return []


print(load_pages("sample.json"))
print(load_pages("abc.json"))
print(load_pages("broken.json"))