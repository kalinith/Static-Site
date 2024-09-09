import unittest

from block_markdown import markdown_to_blocks


class TestBlockMarkup(unittest.TestCase):
    def test_eq(self):
        document = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        result = [
            '# This is a heading',
            'This is a paragraph of text. It has some **bold** and *italic* words inside of it.',
            '''* This is the first list item in a list block
* This is a list item
* This is another list item''',
        ]
        block_lists = markdown_to_blocks(document)
        self.assertEqual(block_lists, result)

if __name__ == "__main__":
    unittest.main()
