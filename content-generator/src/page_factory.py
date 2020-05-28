import file_handler
import header_factory
import content_factory

TAG_CONTENT = "TAG_CONTENT"
TAG_HEADER = "TAG_HEADER"

def make_page(key):
    header = header_factory.make_header(key)
    content = content_factory.make_content(key)
    
    base = file_handler.read("../templates/base.html")
    
    return base.replace(TAG_HEADER, header) \
                .replace(TAG_CONTENT, content) \
