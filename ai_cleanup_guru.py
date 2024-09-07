import os

class DataCleanup:
    content = None
    def __init__(self,content) -> None:
        self.content = content

    def cleanup(self,content) -> str:
        print(content)
        return self.cleanup

    def tokenize_content(self) -> list:
        pass

    def remove_noise(self) -> str:
        pass

    def remove_special_chars(self) -> str:
        pass

    def remove_punctuations(self) -> str:
        pass
