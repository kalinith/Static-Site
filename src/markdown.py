from textnode import TextNode, text_type_text, text_type_code

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
        else:
           split_nodes = []
           text_list = node.text.split(delimiter)
           if len(text_list) % 2 == 0:
               raise Exception(f"invalid markdown syntax found in formatted section")
           for i in range(len(text_list)):
               if text_list[i] == "":
                   continue
               if i % 2 == 0:
                   split_nodes.append(TextNode(text_list[i], text_type_text))
               if i % 2 == 1:
                   split_nodes.append(TextNode(text_list[i], text_type))
           new_nodes.extend(split_nodes)
    return new_nodes
