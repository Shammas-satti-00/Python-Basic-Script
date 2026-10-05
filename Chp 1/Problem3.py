import os

def print_directory_contents(path):
    try:
        entries = os.listdir(path)
        print(f"Contents of '{path}':")
        for entry in entries:
            print(entry)
    except OSError as e:
        print(f"Error accessing directory '{path}': {e}")

if __name__ == "__main__":
    directory = input("Enter the directory path : /").strip()
    if not directory:
        directory = "."  # current working directory
    print_directory_contents(directory)
