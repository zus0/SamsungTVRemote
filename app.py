import json
import argparse
import remote

def interactive(rm):
    def print_help():
        print(
            "\nInteractive shell\n"
            'To run app, start your command with "a"\n'
            'To press a key, type it\n'
            'To get list of all apps, type "g"\n'
            'To get this help message, type "help"\n'
        )
    print_help()

    try:
        while True: #TODO except some invalid input
            command = input("Command (CTRL-D to exit): ")
            
            rm.connect()
            if command == "":
                print("Command is not found!")
            elif command[0:4].upper() == "KEY_":
                command = command
                rm.send_key(command.upper())
            elif command[0].lower() == "a":
                command = command.replace("a ", '')
                rm.start_app(command)
            elif command.lower() == "g":
                print('\n', json.dumps(rm.get_apps(), indent = 2), '\n')
            elif command.lower() == "help":
                print_help()
            else:
                try:
                    rm.send(json.loads(command))
                    print('\n', rm.read_response(), '\n')
                except:
                    print('Invalid JSON')
            rm.close()
            

    except EOFError:
            print()


def main(args):
    rm = remote.SamsungTVRemote(args.ip, args.name)
    shortcuts = rm.shortcuts()
    actions = rm.actions()
    if not args.interactive: rm.connect()

    if args.interactive:
        interactive(rm)
    elif args.shortcut != None:
        getattr(shortcuts, args.shortcut[0])(*args.shortcut[1:])
    elif args.action != None:
        getattr(actions, args.action[0])(*args.action[1:])
    
    rm.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required = True)

    parser.add_argument('ip', help = "IP Adderss of your TV")
    parser.add_argument('name', help="Remote name (default: Python Remote)", nargs="?", const = "Python Remote", default="Python Remote")

    group.add_argument("--shortcut", help = "Shortcut to run", nargs="+")
    group.add_argument("--action", help="Action to run", nargs="+")
    group.add_argument("--interactive", action='store_true', default=False, help = "Interactive shell mode")
    
    args = parser.parse_args()

    main(args)
