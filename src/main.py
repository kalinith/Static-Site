from textnode import *
from htmlnode import *
from file_ops import populate_directory

def main():
    static_files_source = 'static'
    destination_directory = "public"

    node = TextNode("leroy Jenkins", "link","https://192.168.61.129:888")
    print(node)
    html = text_node_to_html_node(node)
    print(html.to_html())

    populate_directory(static_files_source, destination_directory)

main()
