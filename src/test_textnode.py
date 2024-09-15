import unittest

from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        node3 = TextNode("this is the third node","italic","http://google.com")
        node4 = TextNode("this is the third node","italic","http://google.com")
        node5 = TextNode("this is the third node","italic","http://google.com")
        node6 = TextNode("this is the third node","bold","http://google.com")
        node7 = TextNode("this is the third node","italic", None)
        node8 = TextNode("this is the fourth node","italic","http://google.com")
        node9 = TextNode("this is the third node","italic")
        self.assertEqual(node, node2)
        self.assertEqual(node3, node4)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node5, node6)
        self.assertNotEqual(node5, node7)
        self.assertNotEqual(node5, node8)
        self.assertNotEqual(node6, node7)
        self.assertEqual(node7, node9)

    def test_tn_to_hn(self):
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
        result6 = f'<img src="http://lin.tree/image.jpg" alt="this is alt text"></img>'

        self.assertEqual(hnode.to_html(), result)
        self.assertEqual(hnode2.to_html(), result2)
        self.assertEqual(hnode3.to_html(), result3)
        self.assertEqual(hnode4.to_html(), result4)
        self.assertEqual(hnode5.to_html(), result5)
        self.assertEqual(hnode6.to_html(), result6)

if __name__ == "__main__":
    unittest.main()
