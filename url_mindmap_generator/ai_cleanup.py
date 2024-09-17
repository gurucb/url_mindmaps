import os
import cleantext as c

class DataCleanup:
    content = None
    type = None
    def __init__(self) -> None:
        type = "Text Cleanup"
    def cleanup(self,content) -> str:
        self.content = content
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

