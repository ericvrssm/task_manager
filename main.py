import json

def add_name(name):
    # Read existing data (if any)
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []  # Initialize as empty list if file doesn't exist
    
    # Update the data
    data.append(name)  # Add new name to the list
    
    # Write updated data back to the file
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)  # Use indent for readability


add_name('eric')
add_name('emanoelly')