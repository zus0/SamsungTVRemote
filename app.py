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
    actions = rm.actions()
    if not args.interactive: rm.connect()

    if args.interactive:
        interactive(rm)
    elif args.key != None:
        rm.send_key(args.key)
    elif args.app_id != None:
        rm.start_app(args.app)
    elif args.hdmi != None:
        actions.hdmi(args.hdmi)
    elif args.pic_mode != None:
        actions.pic_mode(args.pic_mode)
    
    rm.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required = True)

    parser.add_argument('ip', help = "IP Adderss of your TV")
    parser.add_argument('name', help="Remote name (default: Python Remote)", nargs="?", const = "Python Remote", default="Python Remote")

    group.add_argument("-a", "--app-id", help = "AppId to run")
    group.add_argument("-k", "--key",help = "Key to press")
    group.add_argument("-i", "--interactive", action='store_true', default=False, help = "Interactive shell mode")
    group.add_argument("--hdmi", help="Switch to HDMI", type=int)
    group.add_argument("--pic-mode", help="Picture mode (light/dark)")
    
    args = parser.parse_args()

    main(args)
