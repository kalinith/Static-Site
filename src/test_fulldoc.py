import unittest

from block_markdown import markdown_to_html_node

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        big_test = '''# This is a heading

A This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item

# This is a heading

B This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item

# Hi

## Hi

### Hi

#### Hi

##### Hi

###### Hi

####### Hi

# this is a heading

```this is a code block```

```This is a multi line code block
it is impressive
is it not```

```this is not a code block because it has no ending backticks```

```this is missing starting backticks```

````this one has one backtick````

>this is a quote
>it was written by me
>but the quote isn't
>-Neil 2024

>this starts of as a quote
>however this line is missing a >
>so it doesn't end as a quote

* L first item
* second item
* third item

- M first item
- second item
- third item

- N first item

* O first item
* second item
* third item

* P first
* second
* third
* fourth

1. L first item
2. second item
3. third item
4. fourth item

1. M first item

1. N first item
2 second item

1. O first item
2. second item
3. third item

'''
        expected = '''<div><h1>This is a heading</h1><p>A This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</p><ul><li>This is the first list item in a list block</li><li>This is a list item</li><li>This is another list item</li></ul><h1>This is a heading</h1><p>B This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</p><ul><li>This is the first list item in a list block</li><li>This is a list item</li><li>This is another list item</li></ul><h1>Hi</h1><h2>Hi</h2><h3>Hi</h3><h4>Hi</h4><h5>Hi</h5><h6>Hi</h6><p>####### Hi</p><h1>this is a heading</h1><pre><code>this is a code block</code></pre><pre><code>This is a multi line code block
it is impressive
is it not</code></pre><pre><code>this is not a code block because it has no ending backticks</code></pre><pre><code>this is missing starting backticks</code></pre><pre><code>this one has one backtick</code></pre><blockquote>this is a quote it was written by me but the quote isn't -Neil 2024</blockquote><blockquote>this starts of as a quote however this line is missing a > so it doesn't end as a quote</blockquote><ul><li>L first item</li><li>second item</li><li>third item</li></ul><ul><li>M first item</li><li>second item</li><li>third item</li></ul><ul><li>N first item</li></ul><ul><li>O first item</li><li>second item</li><li>third item</li></ul><ul><li>P first</li><li>second</li><li>third</li><li>fourth</li></ul><ol><li>L first item</li><li>second item</li><li>third item</li><li>fourth item</li></ol><ol><li>M first item</li></ol><p>1. N first item 2 second item</p><ol><li>O first item</li><li>second item</li><li>third item</li></ol></div>'''
        #'''<div><h1>This is a heading</h1><p>A This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</p><ul><li>This is the first list item in a list block</li><li>This is a list item</li><li>This is another list item</li></ul><h1>This is a heading</h1><p>B This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</p><ul><li>This is the first list item in a list block</li><li>This is a list item</li><li>This is another list item</li></ul><h1>Hi</h1><h2>Hi</h2><h3>Hi</h3><h4>Hi</h4><h5>Hi</h5><h6>Hi</h6><p>####### Hi</p><h1>this is a heading</h1><pre><code>this is a code block</code></pre><pre><code>This is a multi line code block it is impressive is it not</code></pre><pre><code>this is not a code block because it has no ending backticks</code></pre><pre><code>this is missing starting backticks</code></pre><pre><code>this one has one backtick</code></pre><blockquote>this is a quote it was written by me but the quote isn't -Neil 2024</blockquote><blockquote>this starts of as a quote however this line is missing a > so it doesn't end as a quote</blockquote><ul><li>L first item</li><li>second item</li><li>third item</li></ul><ul><li>M first item</li><li>second item</li><li>third item</li></ul><ul><li>N first item</li></ul><ul><li>O first item</li><li>second item</li><li>third item</li></ul><ul><li>P first</li><li>second</li><li>third</li><li>fourth</li></ul><ol><li>L first item</li><li>second item</li><li>third item</li><li>fourth item</li></ol><ol><li>M first item</li></ol><p>1. N first item2 second item</p><ol><li>O first item</li><li>second item</li><li>third item</li></ol></div>'''
        result = markdown_to_html_node(big_test)
        self.maxDiff = None
        self.assertEqual(result.to_html(), expected)

if __name__ == "__main__":
    unittest.main()
