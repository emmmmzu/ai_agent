import os


def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    max_chars = 10000
    too_long = max_chars + 1

    try:
        with open(target_file, "r") as f:
            file_content_string = f.read(max_chars)
        with open(target_file, "r") as f:
            truncate = f.read(too_long)
        if len(truncate) > max_chars:
            truncated = str(file_content_string) + '\n[...File "{file_path}" truncated at 10000 characters]'
            return truncated
        return file_content_string
    except Exception as e:
        return f"Error opening file: {e}"
