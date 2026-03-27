# import every .html file from /Keep

import os

def import_files():
    html_files = []
    json_files = []


    for root, dirs, files in os.walk("./Keep"):
        print(f"Checking directory: {root}")
        a = 1
        for file in files:
            print(f"Found file: {file}")
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))
                with open(os.path.join(root, file), "r") as f:
                    all = f.read()
                    title = extract_data(all, "title")
                    content = extract_data(all, "content")


def extract_data(html, class_name):
    start = html.find(f'<div class="{class_name}">') + len(f'<div class="{class_name}">')
    end = html.find('</div>', start)
    return html[start:end]





print("Importing files...")
import_files()


