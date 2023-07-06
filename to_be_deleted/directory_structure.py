import os

def create_directory_structure():
    # Create the top-level directory
    os.makedirs("folder1")
    os.makedirs("folder2")
    os.makedirs("folder3")
    os.makedirs("docs")

    # Create files within folder1
    with open("folder1/file1.txt", "w") as file:
        file.write("This is file1.txt")

    with open("folder1/file2.doc", "w") as file:
        file.write("This is file2.doc")

    # Create files within folder2
    with open("folder2/file3.toml", "w") as file:
        file.write("This is file3.toml")

    with open("folder2/file4.toml", "w") as file:
        file.write("This is file4.toml")

    # Create files within folder3
    with open("folder3/file5.xml", "w") as file:
        file.write("This is file5.xml")

    with open("folder3/file6.toml", "w") as file:
        file.write("This is file6.toml")

    with open("docs/file7.toml", "w") as file:
        file.write("This is file7.toml")

# Call the function to create the directory structure
create_directory_structure()
