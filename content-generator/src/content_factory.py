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

TAG_STYLE_TEXT = "TAG_STYLE_TEXT"
TAG_STYLE_MEDIA = "TAG_STYLE_MEDIA"
TAG_STYLE_CONTAINER = "TAG_STYLE_CONTAINER"

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
    return header + make_divider()

def make_sections(sections):
    result = ""
    
    for i in range(0,len(sections)):
        section = sections[i]
        
        media = make_section_media(section)
        text_style, media_style, container_style = make_style(section)
        extra = make_section_extra(section)

        # create the whole content using the pieces
        content = make_section_content(section, extra, media, text_style, media_style, container_style)
                
        # concat with previous sections' html
        result += content
        
        # if is last, add blank space, else, a divider
        if i == (len(sections) - 1):
            result += make_empty_space()
        else:
            result += make_divider()
    
    return result

def make_section_content(section, extra, media, text_style, media_style, container_style):
    return section_template.replace(TAG_SECTION_TITLE, section["title"]) \
                            .replace(TAG_SECTION_SUBTITLE, section["subtitle"]) \
                            .replace(TAG_SECTION_CONTENT, section["description"]) \
                            .replace(TAG_SECTION_EXTRA, extra) \
                            .replace(TAG_SECTION_MEDIA, media) \
                            .replace(TAG_STYLE_TEXT, text_style) \
                            .replace(TAG_STYLE_MEDIA, media_style) \
                            .replace(TAG_STYLE_CONTAINER, container_style)

def make_section_extra(section):
    keys = section.keys()
    
    # if there is extra content
    if "extra_subtitle" in keys and "extra_description" in keys:
        return section_extra_template.replace(TAG_SECTION_EXTRA_SUBTITLE, section["extra_subtitle"]) \
                                        .replace(TAG_SECTION_EXTRA_DESCRIPTION, section["extra_description"])
    return ""
    
def make_section_media(section):
    if has_media(section):
        
        media_data = section["media_data"]
        
        if media_data["type"] == "image":
            return make_image(media_data)
            
        elif media_data["type"] == "video":
            return make_video(media_data)
            
    return ""
    
def make_image(media_data):
    return "<img class=\"image-" + \
            media_data["position"] + \
            "\" src=\"" + media_data["source"] + "\">"
    
def make_video(media_data):
    return "<br><br><iframe src=\"" + media_data["source"] + "\" width=\"100%\" height=\"480\"></iframe>"

def make_style(section):
    text_style = media_style = "width: 100%;"
    container_style = ""
    
    if has_media(section):
        if section["media_data"]["position"] == "right":
            text_style = "width: 68%;"
            media_style = "width: 32%;"
            container_style = "display: flex;"
            
    else:
        media_style = "width: 0;"
        
    return (text_style, media_style, container_style)

def make_divider():
    divider = file_handler.read("../templates/content_section_divider.html")
    return "\n{}\n".format(divider)
    
def make_empty_space():
    return "<div class=\"blankSpace\"></div"
    
def has_media(section):
    return "media_data" in section.keys()