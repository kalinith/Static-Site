import shutil, os

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
    os.mkdir(directory)
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
            if result != os.path.join(dest_dir, content):
                raise Exception("file not copied")
