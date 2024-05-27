from shell import Shell
import sys

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
        
        if command not in shell.get_commands():
            sys.stdout.write(f"{command}: command not found\n") 
            sys.stdout.flush()
        else:
           shell.run_command(command, args)


if __name__ == "__main__":
    main()
