# list ja map

words = ["this", "is", "a", "list", 10, None, True, (5 != 5), 6.7]
words_map = map(lambda x: str(x), words)
words_str_list = list(words_map)
print(f"'{words_str_list}'")
print(f"'{','.join(words_str_list)}'")
