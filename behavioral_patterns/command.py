class Command:
    def apply(self):
        pass

    def cancel(self):
        pass


class PythonFile:
    def __init__(self, file_name, lines_content):
        self.file_name = file_name
        self.lines_content = lines_content

    def add_line(self, line):
        self.lines_content.append(line)

    def __str__(self):
        return f'{self.file_name}, content: {self.lines_content}'


class RemoveEmptyLinesCommand(Command):
    def __init__(self, file: PythonFile):
        self._file = file

    def apply(self):
        self._file.lines_content = [line for line in self._file.lines_content if line.strip()]

    def cancel(self):
        print('Not supported')


class ChangeFileNameCommand(Command):
    def __init__(self, file: PythonFile, new_name):
        self._file = file
        self._new_name = new_name
        self._previous_name = None

    def apply(self):
        self._previous_name = self._file.file_name
        self._file.file_name = self._new_name
        print(f'Changed name to {self._new_name}')

    def cancel(self):
        if self._previous_name:
            self._file.file_name = self._previous_name
            self._previous_name = None


file = PythonFile('test.py', ['import this', 'print("Hello world")', ''])

changed_name_command = ChangeFileNameCommand(file, 'zen.py')
remove_lines_command = RemoveEmptyLinesCommand(file)

changed_name_command.apply()
remove_lines_command.apply()

print(file)
changed_name_command.cancel()
remove_lines_command.cancel()

print(file)
