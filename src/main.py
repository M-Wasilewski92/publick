import os
import shutil
import sys

from copystatic import copy_files_recursive
from gencontent import generate_page, generate_pages_recursive

base_dir = os.path.abspath(os.path.dirname(__file__))
project_directory = os.path.dirname(base_dir)

dir_path_static = os.path.join(project_directory, "static")
dir_path_public = os.path.join(project_directory, "docs")
dir_path_content = os.path.join(project_directory, "content")
template_path = os.path.join(project_directory, "template.html")



def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating page...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)


if __name__ == '__main__':
    main()
