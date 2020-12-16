from . import create_sequence


class Executor:
    def __init__(self):
        __sequence = []

    def run(self):
        while True:
            result = self.run_once()
            if not result:
                break

    def run_once(self):
        command = input()
        if command.startswith('Create Sequence '):
            return self.__handle_create(command)

        elif command.startswith('Locate '):
            return self.__handle_locate(command)

        elif command == 'Stop':
            return self.__handle_stop(command)
        return True

    def __handle_create(self, command):
        n = int(command.split()[-1])
        self.__sequence = create_sequence(n)
        print(self.__sequence)
        return True

    def __handle_locate(self, command):
        number = int(command.split()[-1])
        try:
            position = self.__sequence.index(number)
            print(f'The number - {number} is at index {position}')
        except ValueError:
            print(f'The number {number} is not in the sequence')
        return True

    def __handle_stop(self, command):
        return False