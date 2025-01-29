#!/usr/bin/env python3

import json
import argparse

parser = argparse.ArgumentParser(description='Task manager for CLI')

parser.add_argument("title", type=str)
parser.add_argument("state", type=str)

args = parser.parse_args()



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



if __name__ == '__main__':
    add_task(args.title, args.state)