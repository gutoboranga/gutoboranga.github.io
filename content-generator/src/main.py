from page_factory import make_page
from file_handler import write as write_file, read_json

# key = "experiences"
# page_content = page_factory.make_page(key)
# filename = "../../{}.html".format(key)
# file_handler.write(filename, page_content)

if __name__ == '__main__':
    pages = read_json("../content/content_index.json")
    
    for page in pages:
        html = make_page(page)
        filename = "../../{}.html".format(page)
        write_file(filename, html)
     