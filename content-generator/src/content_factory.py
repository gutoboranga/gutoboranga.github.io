import file_handler

TAG_SECTION_HEADER_TITLE = "TAG_TITLE"
TAG_SECTION_HEADER_SUBTITLE = "TAG_SUBTITLE"
TAG_SECTION_TITLE = "TAG_TITLE"
TAG_SECTION_SUBTITLE = "TAG_SUBTITLE"
TAG_SECTION_CONTENT = "TAG_CONTENT"


def make_content(key):
    json = file_handler.read_json("../content/{}.json".format(key))
    
    header = make_header(json)
    sections = make_sections(json["sections"])
    
    return header + "\n" + sections
    
    
def make_header(json):
    template = file_handler.read("../templates/content_header.html")
    header = template.replace(TAG_SECTION_HEADER_TITLE, json["title"]) \
                    .replace(TAG_SECTION_HEADER_SUBTITLE, json["subtitle"])
    return header + "\n" + make_divider()

def make_sections(sections):
    template = file_handler.read("../templates/content_section.html")
    content = ""
    
    for section in sections:
        content += template.replace(TAG_SECTION_TITLE, section["title"]) \
                            .replace(TAG_SECTION_SUBTITLE, section["subtitle"]) \
                            .replace(TAG_SECTION_CONTENT, section["description"])
        content += "\n{}\n".format(make_divider())
    return content
    
def make_divider():
    return file_handler.read("../templates/content_section_divider.html")