import argparse

class Program:
    def main(self):
        parser = argparse.ArgumentParser(description='AaaS Command Line Tools.')
        parser.add_argument('--new', dest='feature', action='store_true', help='Create new algorithm from template')

        args = parser.parse_args()

        if(args.feature):
            print("Create new algorithm from template in current directory")


if __name__ == '__main__':
    Program().main()