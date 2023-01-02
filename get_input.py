import json
import requests

def get_input(*args, **kwargs):
    text = Element('test-input').element.value
    print(text)

if __name__ == '__main__':
    get_input()
