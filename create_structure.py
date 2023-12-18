import os
import sys
import json

def create_structure(root_folder, structure):
        for key, value in structure:
            path = os.path.join(root_folder, key)
            if isinstance(value, dict):
                os.makedirs(path, exist_ok=True)
                create_structure(path, value)
            elif isinstance(value, str):
                with open(path, 'w') as file:
                    file.write(value)


def main():
    if len(sys.argv) != 3:
        print("Usage: python create_structure.py root_folder_path structure_json_file_path")
        sys.exit(1)

    root=sys.argv[1]
    structure=sys.argv[2]

    if not os.path.exists(structure):
        print(f"Error: The JSON file '{structure}' does not exist.")
        sys.exit(1)

    with open(structure, 'r') as json_file:
        structure = json.load(json_file)

    if not os.path.exists(root):
        os.makedirs(root)

    create_structure(root, structure)
    print("Folder structure created successfully.")

if __name__ == "__main__":
    main()