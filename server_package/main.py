import sys
sys.path.append('D:/BSUIR/SPOLKS/Lab 1/')

from server_package.server import Server


def main():
    server = Server()
    server.work()


if __name__ == '__main__':
    main()
