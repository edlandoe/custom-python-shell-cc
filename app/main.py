import sys


def main():
    commands = {}
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    # print("Logs from your program will appear here!")

    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    command = input()
    if command not in commands:
       sys.stdout.write(f"{command}: command not found\n") 
       sys.stdout.flush()
    
if __name__ == "__main__":
    main()
