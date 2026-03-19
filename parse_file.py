import re
import json

def parse_markers():
    file = './markers.py'
    pattern = re.compile(r'\@pytest\.mark\.(\w+)')
    try:
        with open(file, 'r') as lines:
            for l in lines:
                match = pattern.match(l)
                if match:
                    print(match[1])
    except FileNotFoundError as e:
        print(f"File not found {e.value}")

def parse_error_logs():
    file = './error_log.log'
    pattern = re.compile(r'(\d{2}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}).*ERROR: (.*)')
    try:
        with open(file, 'r') as lines:
            for l in lines:
                match = pattern.search(l)
                if match:
                    print(f"timestamp: {match[1]}")
                    print(f"Error: {match[2].strip()}")
    except FileNotFoundError as e:
        print(e)

def parse_fio_json():
    file = './fio.json'
    try:
        with open(file, 'r') as jfile:

            json_obj = json.load(jfile)
    except FileNotFoundError as e:
        print(e)

    print(json_obj)
    print(json_obj['jobs'][0]["write"]["iops"])
    # print()

def parse_pod_json():
    file = './pod.json'
    try:
        with open(file, 'r') as jfile:
            json_obj = json.load(jfile)
    except FileNotFoundError as e:
        print(e)

    # print(json_obj)
    print(json_obj['items'][0]["status"]["phase"])
    # print()

# parse_error_logs()
# parse_json()
parse_pod_json()
