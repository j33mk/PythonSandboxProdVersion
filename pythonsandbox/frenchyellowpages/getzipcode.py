import regex as re
address = "17 av Etats Unis, 52000 CHAUMONT, voir sur la carte"

reg = re.compile('^.*(?P<zipcode>\d{5}).*$')
match = reg.match(address)
for key in match.groupdict():
    print((match.groupdict())[key])