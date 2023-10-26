import sys
sys.path.append('D:/BSUIR/SPOLKS/Lab 1/')

from client_package.client import Client


def main():
    client = Client()
    client.work()


if __name__ == '__main__':
    main()
