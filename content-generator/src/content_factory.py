import file_handler

# tags

TAG_SECTION_HEADER_TITLE = "TAG_TITLE"
TAG_SECTION_HEADER_SUBTITLE = "TAG_SUBTITLE"
TAG_SECTION_TITLE = "TAG_TITLE"
TAG_SECTION_SUBTITLE = "TAG_SUBTITLE"
TAG_SECTION_CONTENT = "TAG_CONTENT"

TAG_SECTION_EXTRA = "TAG_EXTRA"
TAG_SECTION_MEDIA = "TAG_MEDIA"
TAG_SECTION_EXTRA_SUBTITLE = "TAG_EXTRA_SUBTITLE"
TAG_SECTION_EXTRA_DESCRIPTION = "TAG_EXTRA_DESCRIPTION"

# templates

section_template = file_handler.read("../templates/content_section.html")
section_extra_template = file_handler.read("../templates/content_section_extra.html")


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
    result = ""
    
    for section in sections:
        media = make_section_media(section)
        extra = make_section_extra(section)
        
        content = make_section_content(section, extra, media)
                
        result += content
        result += "\n{}\n".format(make_divider())
    
    return result

def make_section_content(section, extra, media):
    return section_template.replace(TAG_SECTION_TITLE, section["title"]) \
                            .replace(TAG_SECTION_SUBTITLE, section["subtitle"]) \
                            .replace(TAG_SECTION_CONTENT, section["description"]) \
                            .replace(TAG_SECTION_EXTRA, extra) \
                            .replace(TAG_SECTION_MEDIA, media)

def make_section_extra(section):
    keys = section.keys()
    
    # if there is extra content
    if "extra_subtitle" in keys and "extra_description" in keys:
        return section_extra_template.replace(TAG_SECTION_EXTRA_SUBTITLE, section["extra_subtitle"]) \
                                        .replace(TAG_SECTION_EXTRA_DESCRIPTION, section["extra_description"])
    return ""
    
def make_section_media(section):
    if "media_data" in section.keys():
        media_data = section["media_data"]
        
        if "source" in media_data.keys() and "position" in media_data.keys():
            pass
            
    return ""

def make_divider():
    return file_handler.read("../templates/content_section_divider.html")
    