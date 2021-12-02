# Imports
from app.parsers import args
from app.setup_keeper import Setup_keeper
from app.parser_functions import command


# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


def main():
    Setup_keeper().first_run()
    if args.command != None:
        command[args.command]()


if __name__ == "__main__":
    main()
