import shutil, os
from block_markdown import markdown_to_html_node, extract_title
from inline_markdown import extract_markdown_images, extract_markdown_links

def check_dir_valid(directory):
    if os.path.exists(directory):
        if os.path.isdir(directory):
            return True
        return False
    return None

def clean_dir(directory):
    check = check_dir_valid(directory)
    if check == True:
        shutil.rmtree(directory)
    elif check == False:
        raise Exception(f"{directory} is not a directory")
    os.makedirs(directory)
    print(f"{directory} was created")
    return directory

def populate_directory(source_dir, dest_dir):
    if check_dir_valid(source_dir) == False:
        raise Exception(f"{source_dir} is not a directory")
    dest_path = clean_dir(dest_dir)
    contents_to_transfer = os.listdir(source_dir)
    for content in contents_to_transfer:
        new_source_path = os.path.join(source_dir, content)
        if check_dir_valid(new_source_path):
            new_dest_path = os.path.join(dest_dir, content)
            populate_directory(new_source_path, new_dest_path)
        else:
            result = shutil.copy(new_source_path, dest_dir)
            print(f"{new_source_path} was copied to {result}")
            if result != os.path.join(dest_dir, content):
                raise Exception("file not copied")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    print(f"Reading markdown data from {from_path}........")
    if check_dir_valid(from_path) == False:
        source = open(from_path)
        markdown = source.read()
        source.close()
    else:
        raise Exception("invalid markdown file")

    print(f"Reading template data from {template_path}......")
    if check_dir_valid(template_path) == False:
        source = open(template_path)
        template = source.read()
        source.close()
    else:
        raise Exception("invalid template file")

    print(f"compiling html code")
    division = markdown_to_html_node(markdown)
    content = division.to_html()
    title = extract_title(markdown)
    html_document = template.replace(r"{{ Title }}", title)
    html = html_document.replace(r"{{ Content }}", content)

    print(f"writing htm to {dest_path}.......................")

    if check_dir_valid(dest_path) in (True, None):
        destination = open(dest_path, mode='w')
        destination.write(html)
        destination.close()
    else:
        raise Exception("invalid output file")

    link_list = (extract_markdown_links(markdown))
    site_folder = os.path.dirname(dest_path)
    print(link_list)
    for link in link_list:
        for value in link:
            if value.startswith("/") and len(value) > 1:
                print("dir to add", value)
                dir_to_add = (f"{site_folder}{value}")
                is_dir = check_dir_valid(dir_to_add)
                if is_dir == False:
                    shutil.rmtree(dir_to_add)
                if is_dir != True:
                    os.makedirs(dir_to_add)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if check_dir_valid(dir_path_content) == None:
        raise Exception(f"{dir_path_content} does not exist")
    dirtree = os.listdir(dir_path_content)
    print(dirtree)
    for content in dirtree:
        new_path_content = os.path.join(dir_path_content, content)
        print(f"{content}: {new_path_content}")
        if check_dir_valid(new_path_content):
            print(f"checking if {new_path_content} exists")
            new_dest_dir = os.path.join(dest_dir_path, content)
            if check_dir_valid(new_dest_dir) == False:
                raise Exception(f"{new_dest_dir} does not exist")
            if check_dir_valid(new_dest_dir) != True:
                os.makedirs(new_dest_dir)
                print(f"making new folder {new_dest_dir}")
            generate_pages_recursive(new_path_content, template_path, new_dest_dir)
        else:
            filename = (os.path.splitext(content)[0]+'.html')
            dest_file = os.path.join(dest_dir_path, filename)
            generate_page(new_path_content, template_path, dest_file)
