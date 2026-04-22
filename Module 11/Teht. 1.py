class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, author, name, page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)

    def print_information(self):
        print(f"{super(self.name)}{self.author}{self.page_count}")

class Magazine(Publication):
    def __init__(self, chief_editor, name):
        self.chief_editor = chief_editor
        super().__init__(name)

    def print_information(self):
        print(f"{self.chief_editor}")