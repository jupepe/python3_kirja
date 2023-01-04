# merkkijono listaksi

print("Otetaan esimerkki".split("e"))

print("Otetaan toinen esimerkki".split(" "))

splitted_list = "1;2;3;name;points;date".split(";")
print(splitted_list, " ja listan pituus on ", len(splitted_list))

splitted_list = sorted(splitted_list)
splitted_list.reverse()
print(splitted_list)
