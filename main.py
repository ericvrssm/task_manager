import json


def add_task(title, status):
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    id = len(data)+1
    task = {
            'title': f'{title}',
            'id': f'{id}',
            'status': f'{status}'
        }
    
    process = []
    process.append(task)
    data.append(process)

    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)


def list_task():
    with open('data.json', 'r') as f:
        data = json.load(f)
        list = data.items()
    return print(list)



add_task("fazer o almoço", "fazendo")


