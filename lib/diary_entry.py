class DiaryEntry:
    def __init__(self, title, contents):
        if type(title) != str:
            raise TypeError("title must be a string")
        if type(contents) != str:
            raise TypeError("contents must be a string")
        self.title = title
        self.contents = contents
        self.unread_contents = contents

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        if type(wpm) != int:
            raise TypeError("wpm must be an integer")
        return self.count_words() / wpm
    
    def reading_chunk(self, wpm, minutes):
        words = minutes * wpm
        word_list = self.unread_contents.split()

        if words >= len(word_list):
            self.unread_contents = self.contents
            return " ".join(word_list)
        else:
            chunk = " ".join(word_list[:words])
            self.unread_contents = " ".join(word_list[words:])
            return chunk
        
