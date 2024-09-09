import unittest

from markdown import (
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    split_nodes_delimiter,
    text_to_textnodes,
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

    def test_text_textnodes(self):
        text = 'This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
        nodelist = text_to_textnodes(text)
        result = [
            TextNode("This is ", text_type_text),
            TextNode("text", text_type_bold),
            TextNode(" with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word and a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" and an ", text_type_text),
            TextNode("obi wan image", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", text_type_text),
            TextNode("link", text_type_link, "https://boot.dev"),
        ]
        nodelist2 = text_to_textnodes('**Hobbits**')
        result2 = [TextNode("Hobbits", text_type_bold),]
        nodelist3 = text_to_textnodes('*In* a hole in the ground there lived a hobbit. Not a nasty, dirty, wet hole, filled with the ends')
        result3 = [
            TextNode('In', text_type_italic),
            TextNode(' a hole in the ground there lived a hobbit. Not a nasty, dirty, wet hole, filled with the ends', text_type_text),
        ]
        nodelist4 = text_to_textnodes('of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or to')
        result4 = [TextNode('of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or to', text_type_text),]
        text2 = 'eat: it was a [hobbit-hole](https://en.wikipedia.org/wiki/Hobbit#Lifestyle "Hobbit lifestyles"), and that means comfort.'
        nodelist5 = text_to_textnodes(text2)
        result5 = [
            TextNode('eat: it was a ', text_type_text),
            TextNode('hobbit-hole', text_type_link, 'https://en.wikipedia.org/wiki/Hobbit#Lifestyle "Hobbit lifestyles"'),
            TextNode(', and that means comfort.', text_type_text),
        ]

        self.assertEqual(nodelist, result)
        self.assertEqual(nodelist2, result2)
        self.assertEqual(nodelist3, result3)
        self.assertEqual(nodelist4, result4)
        self.assertEqual(nodelist5, result5)


if __name__ == "__main__":
    unittest.main()

