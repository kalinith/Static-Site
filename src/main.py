from textnode import *
from htmlnode import *

def main():
    node = TextNode("leroy Jenkins", "link","https://192.168.61.129:888")
    print(node)
    html = text_node_to_html_node(node)
    print(html.to_html())

main()
