#!/usr/bin/python3
def text_indentation(text):
    try:
        trav = len(text)
        for p in range(trav):
            if text[p] == '.' or text[p] == '?' or text[p] == ':':
                print('{}\n'.format(text[p]))
            else:
                print('{}'.format(text[p]), end="")
        print()
    except TypeError:
        print('text must be a string')
