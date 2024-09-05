import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(tag="a", props={"href": "https://www.google.com", "target": "_blank",})
        node2 = HTMLNode("a",None,None,{"href": "https://www.google.com", "target": "_blank",})
        node3 = HTMLNode("h1","Heading")
        node4 = HTMLNode("p","This is a paragraph")

        self.assertEqual(node, node2)

    def test_true(self):
        node5 = LeafNode("This is a Leafnode", "p")
        node6 = LeafNode("This is a paragraph of text.", tag="p")
        node7 = LeafNode("Click me!", "a", {"href": "https://www.google.com"})
        node8 = LeafNode("this is plain text")

        print(node5)
        print(f"Node5 should print out as <p>This is a Leafnode</p> : {node5.to_html()}")
        self.assertTrue(node5.to_html() == "<p>This is a Leafnode</p>")
        print(f"Node6 should print out as <p>This is a paragraph of text. : {node6.to_html()}")
        self.assertTrue(node6.to_html() == f"<p>This is a paragraph of text.</p>")
        print(f'Node7 should print out as <a href="https://www.google.com">Click me!</a> : {node7.to_html()}')
        self.assertTrue(node7.to_html() == f'<a href="https://www.google.com">Click me!</a>')
        print(f"Node8 should print out as this is plain text : {node8.to_html()}")
        self.assertTrue(node8.to_html() == f"this is plain text")
