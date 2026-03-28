import os
import json
from datetime import datetime

def import_files():
    json_files = []

    a = False
    for root, dirs, files in os.walk("./Keep"):
        for file in files:
            filename = os.path.join(root, file)
            filename = os.path.splitext(filename)[0]
            filename = filename.replace("./Keep/", "")
            if not a:
                # a = True
                if file.endswith(".json"):
                    with open(os.path.join(root, file), "r") as f:
                        # Get data
                        file = json.load(f)
                        title = file.get('title', 'No title')
                        textcontent = file.get('textContent', 'No text content')
                        createdTimestampUsec = file.get('createdTimestampUsec', 0)
                        userEditedTimestampUsec = file.get('userEditedTimestampUsec', 0)
                        labels = file.get('labels', [])

                        # Validate data
                        if title == '' and textcontent == '':
                            continue
                        if title == '':
                            title = filename
                        
                        # Process data
                        createdTimestampUsec = convert_epoch_to_date(createdTimestampUsec / 1e6)
                        userEditedTimestampUsec = convert_epoch_to_date(userEditedTimestampUsec / 1e6)
                        textcontent = textcontent.split("\n\n")

                        write_file(title, textcontent, createdTimestampUsec, userEditedTimestampUsec, labels)
                else:
                    print(f"Skipping non-JSON file: {filename}")
                    continue
            else:
                break;
                

def convert_epoch_to_date(epoch_time):
    return datetime.fromtimestamp(epoch_time).strftime('%Y%m%d%H%M%S')

def create_id():
    return os.urandom(4).hex()[:7]

def write_file(title, textcontent, createdTimestampUsec, userEditedTimestampUsec, labels):
    file_id = createdTimestampUsec + "-" + create_id()
    children = []
    paragraphs = textcontent if textcontent else [""]

    for index, paragraph in enumerate(paragraphs):
        child_id = userEditedTimestampUsec + "-" + create_id()
        data = paragraph

        children.append({
            "ID": child_id,
            "Type": "NodeParagraph",
            "Properties": {
                "id": child_id,
                "updated": userEditedTimestampUsec
            },
            "Children": [
                {
                    "Type": "NodeText",
                    "Data": data
                }
            ]
        })

    output = {
        "ID": file_id,
        "Spec": "2",
        "Type": "NodeDocument",
        "Properties": {
            "id": file_id,
            "title": title,
            "type": "doc",
            "updated": userEditedTimestampUsec
        },
        "Children": children
    }

    os.makedirs("./output", exist_ok=True)
    with open(f"./output/{file_id}.sy", "w") as f:
        f.write(json.dumps(output, indent=4))



import_files()


