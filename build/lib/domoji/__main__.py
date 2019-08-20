from domoji import *
from crayons import *

def start():
    try:
        menu()
    except KeyboardInterrupt:
        print(red('\nExiting...'))
        exit(1)

if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print(red('\nExiting...'))
        exit(1)