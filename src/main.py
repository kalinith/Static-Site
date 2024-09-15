from textnode import *
from htmlnode import *
from file_ops import populate_directory, generate_pages_recursive

def main():
    content_directory = 'content'
    static_files_directory = 'static'
    destination_directory = "public"
    template = 'template.html'

    node = TextNode("leroy Jenkins", "link","https://192.168.61.129:888")
    print(node)
    html = text_node_to_html_node(node)
    print(html.to_html())

    populate_directory(static_files_directory, destination_directory)
    generate_pages_recursive(content_directory, template, destination_directory)

main()
