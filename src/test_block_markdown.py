import unittest

from block_markdown import markdown_to_blocks, block_to_block_type


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

    def test_block_to(self):
        heading1 = '# Hi'
        heading2 = '## Hi'
        heading3 = '### Hi'
        heading4 = '#### Hi'
        heading5 = '##### Hi'
        heading6 = '###### Hi'
        heading7 = '####### Hi'
        heading8 = '# this is a heading'
        test_code = '```this is a code block```'
        test_code2 = '''```This is a multi line code block
it is impressive
is it not
```'''
        test_code3 = '```this is not a code block because it has no ending backticks'
        test_code4 = 'this is missing starting backticks```'
        test_code5 = '`this one has one backtick`'
        test_quote = """>this is a quote
>it was written by me
>but the quote isn't
>-Neil 2024"""
        test_quote2 = '''>this starts of as a quote
however this line is missing a >
>so it doesn't end as a quote'''
        list_test = '''* first item
* second item
* third item'''
        list_test2 = '''- first item
- second item
- third item'''
        list_test3 = '''- first item
'''
        list_test4 = '''* first item
- second item
_ third item'''
        list_test5 = '''* first
- second
- third
* fourth'''
        o_list_test = '''1. first item
2. second item
3. third item
4. fourth item'''
        o_list_test2 = '''1. first item'''
        o_list_test3 = '''1 first item
2 second item'''
        o_list_test4 = '''`. first item
2 second item
3. third item'''

        self.assertEqual("heading", block_to_block_type(heading1))
        self.assertEqual("heading", block_to_block_type(heading2))
        self.assertEqual("heading", block_to_block_type(heading3))
        self.assertEqual("heading", block_to_block_type(heading4))
        self.assertEqual("heading", block_to_block_type(heading5))
        self.assertEqual("heading", block_to_block_type(heading6))
        self.assertEqual("paragraph", block_to_block_type(heading7))
        self.assertEqual("heading", block_to_block_type(heading8))
        self.assertEqual("code", block_to_block_type(test_code))
        self.assertEqual("code", block_to_block_type(test_code2))
        self.assertEqual("paragraph", block_to_block_type(test_code3))
        self.assertEqual("paragraph", block_to_block_type(test_code4))
        self.assertEqual("paragraph", block_to_block_type(test_code5))
        self.assertEqual("quote", block_to_block_type(test_quote))
        self.assertEqual("paragraph", block_to_block_type(test_quote2))
        self.assertEqual("unordered_list", block_to_block_type(list_test))
        self.assertEqual("unordered_list", block_to_block_type(list_test2))
        self.assertEqual("paragraph", block_to_block_type(list_test3))
        self.assertEqual("paragraph", block_to_block_type(list_test4))
        self.assertEqual("unordered_list", block_to_block_type(list_test5))
        self.assertEqual("ordered_list", block_to_block_type(o_list_test))
        self.assertEqual("ordered_list", block_to_block_type(o_list_test2))
        self.assertEqual("paragraph", block_to_block_type(o_list_test3))
        self.assertEqual("paragraph", block_to_block_type(o_list_test4))

if __name__ == "__main__":
    unittest.main()
