
class Info:
    def __init__(self, user_text):
        self.__user_text = user_text

    @property
    def user_text(self):
        return self.__user_text

    @user_text.setter
    def user_text(self, value):
        if not value.strip():
            raise ValueError("User text cannot be empty")
        self.__user_text = value

    def get_spaces_count(self):
        return self.user_text.count(' ')

    def get_words_count(self):
        return self.get_spaces_count() + 1

    def get_vowels_count(self):
        vowels = 'aeiouAEIOU'
        return sum(1 for char in self.user_text if char in vowels)

    def get_letters_count(self):
        return sum(1 for char in self.user_text if char.isalpha())


def main():
    user_text = input("Please enter a text: ")
    info = Info(user_text)

    print("User Text:", info.user_text)
    print("Spaces Count:", info.get_spaces_count())
    print("Words Count:", info.get_words_count())
    print("Vowels Count:", info.get_vowels_count())
    print("Letters Count:", info.get_letters_count())


if __name__ == "__main__":
    main()
