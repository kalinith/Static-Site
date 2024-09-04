import unittest

from textnode import TextNode


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

if __name__ == "__main__":
    unittest.main()
