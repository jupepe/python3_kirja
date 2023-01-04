# Esimerkki: Suomi-Englanti -Sanakirja

class FiEnDictionary:
    def __init__(self, langs):
        self.__langs = langs

    def __get_reversed_dictionary(self):  # privaatti metodi
        return {en: fi for fi, en in self.__langs.items()}

    def get_en(self, word):
        return self.__langs.get(word)

    def get_fi(self, word):
        langs_rev = self.__get_reversed_dictionary()
        return langs_rev.get(word)

    def set_word(self, fi_word, en_word):
        if fi_word and en_word:
            self.__langs[fi_word] = en_word


init_langs = {'ohjelmointi': 'programming', 'luokka': 'class', 'olio': "object", "kieli": "language"}

fi_en_dict = FiEnDictionary(init_langs)
fi_en_dict.set_word("funktio", "function")
fi_en_dict.set_word("argumentti", "argument")
pr_fi = fi_en_dict.get_fi('programming')
fun_fi = fi_en_dict.get_fi('function')
dia_fi = fi_en_dict.get_fi('diagram')
fun_en = fi_en_dict.get_en('funktio')
print(f"programming: {pr_fi}")
print(f"function:\t {fun_fi}")
print(f"diagram:\t {dia_fi}")
print(f"funktio:\t {fun_en}")
