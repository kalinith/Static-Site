import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(tag="a", props={"href": "https://www.google.com", "target": "_blank",})
        node2 = HTMLNode("a",None,None,{"href": "https://www.google.com", "target": "_blank",})
        node3 = HTMLNode("h1","Heading")
        node4 = HTMLNode("p","This is a paragraph")

        print(node)
