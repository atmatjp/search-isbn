import requests
import sys

def get_bookinfo(isbn):
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
    
    response = requests.get(url)
    
    data = response.json()
    
    if "items" in data and len(data["items"]) > 0:
        title = data["items"][0]["volumeInfo"]["title"]
        authors = data["items"][0]["volumeInfo"]["authors"]
        return f"{title} : {authors}"    
    else:
        return "何の本を読んでるんだ？"

def main():
    input_isbn = input()
    if len(input_isbn) == 13:
        isbn = input_isbn
        book_info = get_bookinfo(isbn)
        print(book_info)    
    else:
        print(f"13文字の半角数字を入力してください")
        sys.exit(1)

if __name__ == "__main__":
    main()