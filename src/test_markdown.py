import unittest

from markdown import split_nodes_delimiter
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
    )

class TestMarkup(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        result = [
            TextNode("This is text with a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" word", text_type_text),
        ]

        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertEqual(new_nodes, result)

#    def test_ex(self):
#        node2 = TextNode("This is *a text with a `code block` word",text_type_text)
#        msg = "Exception('invalid markdown syntax found in formatted section'"
#        try:
#            split_nodes_delimiter([node2], "*", text_type_code)
#        except Exception as e:
#            self.assertEqual(e, msg)


if __name__ == "__main__":
    unittest.main()

