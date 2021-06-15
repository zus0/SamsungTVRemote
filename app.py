import json
import argparse
import remote

def interactive(remote):
    def print_help():
        print(
            "\nInteractive shell\n"
            'To run app, start your command with "a"\n'
            'To press a key, type it\n'
            'To get list of all apps, type "g"\n'
            'To get this help message, type "help"'
        )
    print_help()

    try:
        while True: #TODO except some invalid input
            command = input("Command (CTRL-D to exit): ")
            
            if command == "":
                print("Command is not found!")
            elif command[0:4].upper() == "KEY_":
                command = command
                remote.send_key(command.upper())
            elif command[0].lower() == "a":
                command = command.replace("a ", '')
                remote.start_app(command)
            elif command.lower() == "g":
                remote.get_apps()
                print('\n', json.dumps(remote.read_response(), indent = 2), '\n')
            elif command.lower() == "help":
                print_help()
            else:
                try:
                    remote.send(json.loads(command))
                    print('\n', remote.read_response(), '\n')
                except:
                    print('Invalid JSON')

    except EOFError:
            print()


def main(args):
    rm = remote.SamsungTVRemote(args.ip, args.name)
    rm.connect()

    if args.i:
        interactive(rm)
    elif args.k != None:
        rm.send_key(args.key)
    elif args.a != None:
        rm.start_app(args.app)
    
    rm.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required = True)

    parser.add_argument('ip', help = "IP Adderss of your TV")
    parser.add_argument('name', help="Remote name (default: Python Remote)", nargs="?", const = "Python Remote", default="Python Remote")

    group.add_argument("-a", "--app_id", help = "AppId to run")
    group.add_argument("-k", "--key",help = "Key to press")
    group.add_argument("-i", "--interactive", action='store_true', default=False, help = "Interactive shell mode")
    
    args = parser.parse_args()

    main(args)
