import os
import sys
import subprocess

def list_directory():
    subprocess.run(["ls"])

def change_directory(path):
    try:
        os.chdir(path)
    except FileNotFoundError:
        print(f"Directory '{path}' not found")

def read_file(filename):
    subprocess.run(["cat", filename])

def echo_message(message):
    print(message)

def make_directory(dirname):
    subprocess.run(["mkdir", dirname])

def remove_directory(dirname):
    subprocess.run(["rmdir", dirname])

def copy_file(src, dest):
    subprocess.run(["cp", src, dest])

def move_file(src, dest):
    subprocess.run(["mv", src, dest])

def remove_file(filename):
    subprocess.run(["rm", filename])

def print_working_directory():
    subprocess.run(["pwd"])

def list_processes():
    subprocess.run(["ps", "aux"])

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

