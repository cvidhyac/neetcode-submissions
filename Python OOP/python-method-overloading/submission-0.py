class TextProcessor:
    # Implement method overloading for format_text method
    def format_text(self, a, b=None):
        if b is None:
            return a.upper()
        else:
            return a + b



# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
