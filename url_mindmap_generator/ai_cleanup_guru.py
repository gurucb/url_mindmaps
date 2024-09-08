import os
import cleantext as c

class DataCleanup:
    content = None
    def __init__(self,content) -> None:
        self.content = content

    def cleanup(self,content) -> str:
        self.content = c.clean(
                                content,
                                extra_spaces=True,
                                stopwords=True,
                                lowercase=True,
                                numbers=True,
                                punct=True
                                )
        return self.content

    def tokenize_content(self) -> list:
        pass

    def remove_noise(self) -> str:
        pass

