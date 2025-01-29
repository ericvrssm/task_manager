#!/usr/bin/env python3

import json
import argparse

parser = argparse.ArgumentParser(description='Task manager for CLI')


#general commands
parser.add_argument("-t", "--title")
parser.add_argument("-s","--state")
parser.add_argument('-l', '--list')


def liste():
    with open('data.json', 'r') as f:
         data = json.load(f)
    if isinstance(data, list):
        for sublist in data:
            if isinstance(sublist, list):
                for item in sublist:
                    if isinstance(item, dict) and "id" in item:
                        print(f"{item["id"]}. {item['title']}")

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


args = parser.parse_args()
if __name__ == '__main__':
    add_task(args.title, args.state)
    liste(args.list)