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

def exit_sysco():
    print("Exiting Sysco Command Prompt")
    sys.exit()

# Command dictionary
commands = {
    'ls': list_directory,
    'cd': change_directory,
    'cat': read_file,
    'echo': echo_message,
    'exit': exit_sysco
}

def main():
    print("Sysco Command Prompt")
    while True:
        current_dir = os.getcwd()
        command_input = input(f"{current_dir} $ ").strip().split()
        if not command_input:
            continue

        cmd = command_input[0]
        args = command_input[1:]

        if cmd in commands:
            try:
                if args:
                    commands[cmd](*args)
                else:
                    commands[cmd]()
            except TypeError:
                print(f"Invalid arguments for command: {cmd}")
        else:
            print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
