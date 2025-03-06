from textnode import *
from htmlnode import *
import sys

from file_ops import populate_directory, generate_pages_recursive

def main():
    content_directory = 'content'
    static_files_directory = 'static'
    destination_directory = 'docs'
    template = 'template.html'
    basepath = '/'

    if len(sys.argv) == 2:
        basepath = sys.argv[1]

    populate_directory(static_files_directory, destination_directory)
    generate_pages_recursive(content_directory, template, destination_directory, basepath)

main()
