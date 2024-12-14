import os
import sys
import requests

# Function to execute bash commands via API
def execute_command(command):
    response = requests.post('http://localhost:3000/execute', json={'command': command})
    if response.status_code == 200:
        return response.json()['output']
    else:
        return response.json()['error']

# Command functions
def list_directory():
    print(execute_command('ls'))

def change_directory(path):
    try:
        os.chdir(path)
        print(execute_command('pwd'))
    except FileNotFoundError:
        print(f"Directory '{path}' not found")

def read_file(filename):
    print(execute_command(f'cat {filename}'))

def echo_message(message):
    print(message)

def make_directory(dirname):
    print(execute_command(f'mkdir {dirname}'))

def remove_directory(dirname):
    print(execute_command(f'rmdir {dirname}'))

def copy_file(src, dest):
    print(execute_command(f'cp {src} {dest}'))

def move_file(src, dest):
    print(execute_command(f'mv {src} {dest}'))

def remove_file(filename):
    print(execute_command(f'rm {filename}'))

def print_working_directory():
    print(execute_command('pwd'))

def list_processes():
    print(execute_command('ps aux'))

def exit_sysco():
    print("Exiting Sysco Command Prompt")
    sys.exit()

# Command dictionary
commands = {
    'ls': list_directory,
    'cd': change_directory,
    'cat': read_file,
    'echo': echo_message,
    'mkdir': make_directory,
    'rmdir': remove_directory,
    'cp': copy_file,
    'mv': move_file,
    'rm': remove_file,
    'pwd': print_working_directory,
    'ps': list_processes,
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


