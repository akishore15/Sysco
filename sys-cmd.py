import os
import sys

def list_directory():
    for item in os.listdir():
        print(item)

def change_directory(path):
    try:
        os.chdir(path)
    except FileNotFoundError:
        print(f"Directory '{path}' not found")

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"File '{filename}' not found")

def echo_message(message):
    print(message)

def main():
    print("Sysco Command Prompt")
    while True:
        current_dir = os.getcwd()
        command = input(f"{current_dir} $ ").strip().split()
        if not command:
            continue

        cmd = command[0]
        args = command[1:]

        if cmd == 'ls':
            list_directory()
        elif cmd == 'cd':
            if args:
                change_directory(args[0])
            else:
                print("Please specify a directory")
        elif cmd == 'cat':
            if args:
                read_file(args[0])
            else:
                print("Please specify a file")
        elif cmd == 'echo':
            echo_message(' '.join(args))
        elif cmd == 'exit':
            print("Exiting Sysco Command Prompt")
            sys.exit()
        else:
            print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
