import sys

def exit(args: str):
    if args:
        sys.exit(int(args[0]))
    
def echo(args: str):
    sys.stdout.write(f"{" ".join(args)}\n")
    sys.stdout.flush()
    
def type(args: str):
    if args[0] in commands:
        sys.stdout.write(f"{args[0]} is a shell builtin\n")
        sys.stdout.flush()
    else:
        sys.stdout.write(f"{args[0]} not found\n")
        sys.stdout.flush()
        
commands = {
        "exit": exit,
        "echo": echo,
        "type": type
    }

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        initial_input = input()  # Wait for user input 
        command = initial_input.split(" ")[0]
        args = []
        if len(initial_input.split(" ")) > 1:
            args = initial_input.split(" ")[1:]
        
        if command not in commands:
            sys.stdout.write(f"{command}: command not found\n") 
            sys.stdout.flush()
        else:
            commands[command](args)


if __name__ == "__main__":
    main()
