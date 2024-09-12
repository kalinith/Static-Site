import re

from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode

block_type_paragraph = 'paragraph'
block_type_heading = 'heading'
block_type_code = 'code'
block_type_quote = 'quote'
block_type_unordered_list = 'unordered_list'
block_type_ordered_list = 'ordered_list'

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block):
    block_type = block_type_paragraph
    if re.match(r'^#{1,6} ', block):
        block_type = block_type_heading

    if len(block) >= 6 and block[0:3] == '```' and block[-1:-4:-1] == '```':
        block_type = block_type_code

    quote_lines = re.findall(r'^>', block, flags=re.M)
    if len(quote_lines) == len(block.split("\n")):
        block_type = block_type_quote

    u_list_lines = re.findall(r'^\* |^\- ', block, flags=re.M)
    if len(u_list_lines) == len(block.split("\n")):
        block_type = block_type_unordered_list

    o_list_lines = block.split("\n")
    newlist = list()
    for i in range(len(o_list_lines)):
        if len(o_list_lines[i]) < 3:
           continue
        if str(i+1) == o_list_lines[i][0] and o_list_lines[i][1:3] == ". ":
           newlist.append(o_list_lines[i])
    if len(newlist) == len(o_list_lines):
        block_type = block_type_ordered_list
    return block_type

def text_to_children(text):
    html_children = list()
    textnodes = text_to_textnodes(text)
    for node in textnodes:
        html_children.append(text_node_to_html_node(node))
    return html_children


def markdown_to_html_node(markdown):
    children = list()
    document_blocks = markdown_to_blocks(markdown)
    for block in document_blocks:
        block_type = block_to_block_type(block)

        if block_type == block_type_paragraph:
            text_list = block.split("\n")
            text = " ".join(text_list)
            children.append(ParentNode('p',text_to_children(text),None))
        if block_type == block_type_heading:
            if block.startswith('###### '):
                children.append(ParentNode('h6', text_to_children(block[7:]),None))
            elif block.startswith('##### '):
                children.append(ParentNode('h5', text_to_children(block[6:]),None))
            elif block.startswith('#### '):
                children.append(ParentNode('h4', text_to_children(block[5:]),None))
            elif block.startswith('### '):
                children.append(ParentNode('h3', text_to_children(block[4:]),None))
            elif block.startswith('## '):
                children.append(ParentNode('h2', text_to_children(block[3:]),None))
            elif block.startswith('# '):
                children.append(ParentNode('h1', text_to_children(block[2:]),None))
        if block_type == block_type_code:
            code_body = block.strip('`')
            code = (ParentNode('code', text_to_children(code_body), None),)
            pre = ParentNode('pre', code, None)
            children.append(pre)
        if block_type == block_type_quote:
            line_list = block.split('\n')
            clean_line_list = list(map(lambda x: x.lstrip('>').strip(), line_list))
            quote_body = ' '.join(clean_line_list)
            quote = ParentNode('blockquote', text_to_children(quote_body), None)
            children.append(quote)
        if block_type == block_type_unordered_list:
            list_items = block.split('\n')
            list_line = list()
            for item in list_items:
                itemnodes = text_to_children(item[2:])
                li = ParentNode('li', itemnodes, None)
                list_line.append(li)
            children.append(ParentNode('ul',list_line,None))
        if block_type == block_type_ordered_list:
            list_items = block.split('\n')
            list_line = list()
            for item in list_items:
                itemnodes = text_to_children(item[3:])
                li = ParentNode('li', itemnodes, None)
                list_line.append(li)
            children.append(ParentNode('ol',list_line,None))
    div = ParentNode('div',children,None)
    return div
