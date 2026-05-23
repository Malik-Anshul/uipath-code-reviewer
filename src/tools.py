def read_file(file_path):
    file_path = file_path.strip('"')

    if not file_path.endswith(".py"):
        return False, "Please provide a .py file"
    
    try:
        with open(file_path) as f:
            file_data = f.read()
        
        if not file_data.strip():
            return False, "File is empty"
        
        return True, file_data

    except FileNotFoundError:
        return False, "File not found"
    except Exception as e:
        return False, f"Error reading file: {str(e)}"

    