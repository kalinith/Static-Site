import unittest

from markdown import (
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    split_nodes_delimiter,
    )
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

    def test_link_eq(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        text2 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(extract_markdown_images(text),[("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])
        self.assertEqual(extract_markdown_images(text2),[])

    def test_links_eq(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        text2 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(extract_markdown_links(text), [])
        self.assertEqual(extract_markdown_links(text2), [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])

    def test_image_split(self):
        node = TextNode(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        result = [
            TextNode("This is text with a ", text_type_text),
            TextNode("rick roll", text_type_image, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", text_type_text),
            TextNode("obi wan", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        self.assertEqual(new_nodes, result)

    def test_link_split(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            text_type_text,
        )
        new_nodes = split_nodes_link([node])
        result = [
        TextNode("This is text with a link ", text_type_text),
        TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
        TextNode(" and ", text_type_text),
        TextNode(
            "to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"
        )
        ]
        self.assertEqual(new_nodes, result)

if __name__ == "__main__":
    unittest.main()

