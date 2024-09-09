import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

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


def extract_markdown_images(text):
    image_values = []
    for result in re.findall(r'!\[(.*?)\]\((.*?)\)', text):
        image_values.append(result)
    return image_values


def extract_markdown_links(text):
    link_values = []
    for result in re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text):
        link_values.append(result)
    return link_values


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        image_list = extract_markdown_images(node.text)
        if image_list == []:
            new_nodes.append(node)
            continue
        split_nodes = []
        text_list = re.split(r'!\[.*?\]\(.*?\)', node.text)
        for text in text_list:
            if text != "":
                split_nodes.append(TextNode(text, text_type_text))
            if len(image_list) != 0:
                img_text, img_url = image_list.pop(0)
                split_nodes.append(TextNode(img_text,text_type_image,  img_url))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        link_list = extract_markdown_links(node.text)
        if link_list == []:
            new_nodes.append(node)
            continue
        split_nodes = []
        text_list = re.split(r'(?<!!)\[.*?\]\(.*?\)', node.text)
        for text in text_list:
            if text != "":
                split_nodes.append(TextNode(text, text_type_text))
            if len(link_list) != 0:
                alt_text, url = link_list.pop(0)
                split_nodes.append(TextNode(alt_text,text_type_link,  url))
        new_nodes.extend(split_nodes)
    return new_nodes

def text_to_textnodes(text):
    initial_node = []
    initial_node.append(TextNode(text, text_type_text))
    image_nodes = split_nodes_image(initial_node)
    link_nodes = split_nodes_link(image_nodes)
    bold_nodes = split_nodes_delimiter(link_nodes, '**', text_type_bold)
    ital_nodes = split_nodes_delimiter(bold_nodes, '*', text_type_italic)
    list_of_nodes = split_nodes_delimiter(ital_nodes, '`', text_type_code)
    return list_of_nodes

