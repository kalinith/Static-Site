import re

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


