import copy


class PythonCodeFile:
    def __init__(self, license_content, file_extension, code='', file_name=''):
        self._license_content = license_content
        self._file_extension = file_extension
        self._code = code
        self._file_name = file_name

    @property
    def license_content(self):
        return self._license_content

    @license_content.setter
    def license_content(self, value):
        self._license_content = value

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value

    @property
    def file_extension(self):
        return self._file_extension

    @file_extension.setter
    def file_extension(self, value):
        self._file_extension = value

    def create_clone(self):
        return copy.copy(self)

    def __str__(self):
        return (
            f"File: {self._file_name}.{self.file_extension}, License: {self._license_content}"
            f", Code: {self._code}"
        )


class PythonCodeFileManager:
    _base_file = PythonCodeFile('BSD', 'py')

    @staticmethod
    def create_file_with_content(file_name, code):
        base_file_clone = PythonCodeFileManager._base_file.create_clone()
        base_file_clone.file_name = file_name
        base_file_clone.code = code
        return base_file_clone


file_1 = PythonCodeFileManager.create_file_with_content('zen_of_python', 'import this')
file_2 = PythonCodeFileManager.create_file_with_content('test_file', 'just testing')

print(file_1)
print(file_2)
