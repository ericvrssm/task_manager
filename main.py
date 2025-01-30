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
parser.add_argument('-rm', '--remove', action="store_true", help="remove a task based on an ID")
parser.add_argument('-i', '--id', type=int)

def liste():
    data = setup()
    if isinstance(data, list):
        for item in data:
            print(f"{item["id"]}. {item['title']} : {item['status']}")

def add_task(title, status):

    data = setup()
    id = len(data)+1
    task = {
            'title': f'{title}',
            'id': id,
            'status': f'{status}'
        }
    
    process = []
    process.append(task)
    data.append(task)

    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)

def remove_task(id):
    index = id-1
    new_data = []
    with open('data.json', 'r') as f:
        data = json.load(f)
    
    for i in range(len(data)):
        if index == i:
            i+=1
        else:
            new_data.append(data[i])
            for j in range(len(new_data)):
                temp = j
                reord = new_data[temp]
                reord['id'] = j+1
                j+=1
            i+=1
    



    with open('data.json', 'w') as f:
            json.dump(new_data, f, indent=4)



args = parser.parse_args()
if __name__ == '__main__':
    if args.addtask == True:
        add_task(args.title, args.state)
    elif args.list == True:
        liste()
    elif args.remove == True:
        remove_task(args.id)