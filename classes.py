class File:
    def __init__(self, file_name):
        self.file_name = file_name

    def readFile(self):
        try:
            with open(self.file_name) as file_to_read:
                all_contents = file_to_read.read()
        except FileNotFoundError:
            pass
        else:
            return all_contents

    def readFileLines(self):
        try:
            with open(self.file_name) as file_to_read:
                list_of_lines = []
                all_lines = file_to_read.readlines()
                for line in all_lines:
                    list_of_lines.append(line.rstrip())
        except FileNotFoundError:
            pass
        else:
            return list_of_lines

    def writeToFile(self, write_text):
        with open(self.file_name, 'w') as file_to_write_into:
            writings = file_to_write_into.write(write_text)
        return writings

    def appendFile(self, lines_to_append):
        with open(self.file_name) as file_to_append:
            appended = file_to_append.write(lines_to_append)
        return appended


class Files(File):
    def __init__(self, file_list):
        self.file_list = file_list

    def readLinesInFiles(self):
        for file in self.file_list:
            File(file)
            File.readFileLines(self)              

