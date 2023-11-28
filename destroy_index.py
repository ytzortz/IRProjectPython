import shutil

def delete_directory(directory_path):
    try:
        shutil.rmtree(directory_path)
        print(f"Directory '{directory_path}' successfully deleted.")
    except FileNotFoundError:
        print(f"Directory '{directory_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the path to the directory you want to delete
directory_to_delete = "index"

# Call the function to delete the directory
delete_directory("../index")