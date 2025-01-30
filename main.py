#!/usr/bin/env python3

import json
import argparse
def setup():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        with open('data.json', 'w') as f:
            data = []
            json.dump(data , f)
    except FileNotFoundError:
        data = []
    return data

parser = argparse.ArgumentParser(description='Task manager for CLI')
#general commands
parser.add_argument("-a", "--addtask", action="store_true", help="add a task to the database")
parser.add_argument("-t", "--title")
parser.add_argument("-s","--state")
parser.add_argument('-l', '--list', action="store_true", help="list all the tasks by id and their status")


def liste():
    data = setup()
    if isinstance(data, list):
        for sublist in data:
            if isinstance(sublist, list):
                for item in sublist:
                    if isinstance(item, dict) and "id" in item:
                        print(f"{item["id"]}. {item['title']} : {item['status']}")

def add_task(title, status):

    data = setup()
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

def remove_task(id):
    setup()




args = parser.parse_args()
if __name__ == '__main__':
    if args.addtask == True:
        add_task(args.title, args.state)
    if args.list == True:
        liste()