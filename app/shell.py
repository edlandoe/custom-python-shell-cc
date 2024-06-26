from typing import Callable
import sys, os

class Shell:
    def __init__(self):
        self.commands = {
        "exit": self.exit,
        "echo": self.echo,
        "type": self.type
    }
    
    # Helper Functions        
    def _get_command_path(self, command: str) -> str | None: 
        env_var = os.getenv("PATH")
        directories = env_var.split(":")
        
        for directory in directories:
            path = os.path.join(directory, command)
            if os.path.exists(path):
                return path
            
        return None
        
    # Class Functions
    def get_commands(self) -> dict[str, Callable[[list[str]], None]]:
        return self.commands
    
    def run_command(self, command: str, args: list[str]) -> Callable[[list[str]], None]:
        return self.commands[command](args)
      
    def exit(self, args: list[str]) -> None:
        if args:
            sys.exit(int(args[0]))
        
    def echo(self, args: list[str]) -> None:
        sys.stdout.write(f"{' '.join(args)}\n")
        sys.stdout.flush()
       
    def type(self, args: list[str]) -> None:
        if args[0] in self.commands:
            sys.stdout.write(f"{args[0]} is a shell builtin\n")
            sys.stdout.flush()
        elif path := self._get_command_path(args[0]):
            sys.stdout.write(f"{args[0]} is {path}\n")
            sys.stdout.flush()
        else:
            sys.stdout.write(f"{args[0]} not found\n")
            sys.stdout.flush()
            
    def execute_path(self, path, args) -> None:
        os.system(f"{path} {' '.join(args)}")
            