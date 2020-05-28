import file_handler

TAG_TABS = "TAG_PAGES_INDEX"
TAG_TAB_REF = "TAG_REF"
TAG_TAB_TITLE = "TAG_TITLE"
TAG_TAB_CLASS = "TAG_CLASS"
TAG_EXTRA = "TAG_EXTRA"

def make_header(current_tab=None):
    template = file_handler.read("../templates/header.html")
    tabs_html = make_tabs(current_tab)
    return template.replace(TAG_TABS, tabs_html, 1)


def make_tabs(current_tab=None):
    pages = file_handler.read_json("../content/content_index.json")
    template = file_handler.read("../templates/header_index.html")
    content = ""
    
    for key in pages:
        css_class = "button"
        extra = ""
        
        if current_tab == key:
            css_class += " button-selected"
            extra = "<div id=\"little-circle\"></div>"
        
        content += template.replace(TAG_TAB_REF, pages[key]["ref"]) \
                            .replace(TAG_TAB_TITLE, pages[key]["title"]) \
                            .replace(TAG_TAB_CLASS, css_class) \
                            .replace(TAG_EXTRA, extra) \
                            + "&emsp;"
                            
        
    
    return content
