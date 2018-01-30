def sentence(inp):
    words = inp.split()
    b = len(words)
    c = int((0+b)/2)
    print(words[c])


sent = input("enter:")
sentence(sent)
