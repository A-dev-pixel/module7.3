class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_names in self.file_names:
            with open(file_names, "r", encoding="utf-8") as file:
                line = file.read().lower()
                new = [',', '.', '=', '!', '?', ';', ':', ' - ']
                for new_s in new:
                    line = line.replace(new_s, '')
                new_q = line.split()
                all_words[file_names] = new_q
        return all_words

    def find(self, word):
        new_r = {}
        new_f = self.get_all_words().items()
        for name, words in new_f:
            new_r[name] = words.index(word.lower()) + 1
        return new_r

    def count(self, word):
        new_u = {}
        new_k = self.get_all_words().items()
        for name, words in new_k:
            new_u[name] = words.count(word.lower())
        return new_u


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
