
import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode
from main import *

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("this is plain text", "text")
        hnode = text_node_to_html_node(node)
        result = "this is plain text"
        node2 = TextNode("italic word", "italic")
        hnode2 = text_node_to_html_node(node2)
        result2 = f"<i>italic word</i>"
        node3 = TextNode("This is a bold statement", "bold")
        hnode3 = text_node_to_html_node(node3)
        result3 = f"<b>This is a bold statement</b>"
        node4 = TextNode("Hello World!", "code")
        hnode4 = text_node_to_html_node(node4)
        result4 = f"<code>Hello World!</code>"
        node5 = TextNode("some anchor text", "link", "http://link.tree")
        hnode5 = text_node_to_html_node(node5)
        result5 = f'<a href="http://link.tree">some anchor text</a>'
        node6 = TextNode("this is alt text", "image", "http://lin.tree/image.jpg")
        hnode6 = text_node_to_html_node(node6)
        result6 = f'<img src="http://lin.tree/image.jpg" alt="this is alt text">'

        self.assertEqual(hnode.to_html(), result)
        self.assertEqual(hnode2.to_html(), result2)
        self.assertEqual(hnode3.to_html(), result3)
        self.assertEqual(hnode4.to_html(), result4)
        self.assertEqual(hnode5.to_html(), result5)
        self.assertEqual(hnode6.to_html(), result6)

