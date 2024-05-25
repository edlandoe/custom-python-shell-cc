import sys


def main():
    commands = {}

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        command = input()
        if command not in commands:
            sys.stdout.write(f"{command}: command not found\n") 
            sys.stdout.flush()
    
if __name__ == "__main__":
    main()
