import sys

def exit(args = ""):
    if args[0] == "0":
        sys.exit(0)
    else:
        sys.stdout.write(f"Need proper arguments\n")
    
    
def main():
    commands = {
        "exit": exit
    }

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        initial_input = input()  # Wait for user input 
        command = initial_input.split(" ")[0]
        args = [""]
        if len(command) > 1:
            args = initial_input.split(" ")[1:]
        
        if command not in commands:
            sys.stdout.write(f"{command}: command not found\n") 
            sys.stdout.flush()
        else:
            commands[command](args)


if __name__ == "__main__":
    main()
