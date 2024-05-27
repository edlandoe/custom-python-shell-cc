from shell import Shell
import sys, os

def main():
    shell = Shell()   
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        initial_input = input().split(" ")  # Wait for user input 
        command = initial_input[0]
        args = []
        
        if len(initial_input) > 1:
            args = initial_input[1:]
        
        if command in shell.get_commands():
            shell.run_command(command, args)
        else: 
            if os.path.exists(command):
                shell.execute_path(command, args)
            else: 
                print(f"{command}: command not found")


if __name__ == "__main__":
    main()
