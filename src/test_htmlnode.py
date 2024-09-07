import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(tag="a", props={"href": "https://www.google.com", "target": "_blank",})
        node2 = HTMLNode("a",None,None,{"href": "https://www.google.com", "target": "_blank",})
        node3 = HTMLNode("h1","Heading")
        node4 = LeafNode(tag="p",value="This is a paragraph")

        self.assertEqual(node, node2)
        nodetest = node4.to_html()
        self.assertEqual(nodetest, "<p>This is a paragraph</p>")

    def test_true(self):
        node5 = LeafNode("p", "This is a Leafnode",)
        node6 = LeafNode(value="This is a paragraph of text.", tag="p")
        node7 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        node8 = LeafNode(None, "this is plain text")
        node9 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        node10 = ParentNode(
            tag="p",
            children=
                [
                    LeafNode(tag="b", value="Bold text"),
                    LeafNode(tag=None, value="Normal text"),
                    LeafNode(tag="i", value="italic text"),
                    LeafNode(tag=None, value="Normal text"),
                ]
        )
        node11 = ParentNode(
            "p",
                [
                    ParentNode(
                        "i",
                        [
                            LeafNode(tag="b", value="Boldly Going"),
                        ],
                    ),
                    LeafNode(tag=None, value="nowhere"),
                    LeafNode(tag="i", value="slowly"),
                 ],
            )
        self.assertTrue(node5.to_html() == "<p>This is a Leafnode</p>")
        self.assertTrue(node6.to_html() == f"<p>This is a paragraph of text.</p>")
        self.assertTrue(node7.to_html() == f'<a href="https://www.google.com">Click me!</a>')
        self.assertTrue(node8.to_html() == f"this is plain text")
        self.assertTrue(node9.to_html() == node10.to_html())
        self.assertTrue(node11.to_html() == "<p><i><b>Boldly Going</b></i>nowhere<i>slowly</i></p>")
