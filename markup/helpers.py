'''
Helper functions to add markup to blog posts
'''
from html import HTML


def add_paragraph_elements(post_string):
    paragraph_list = post_string.split("\r\n\r\n")

    rmelements = []
    for i in range(len(paragraph_list)):
        if paragraph_list[i] != "":
            paragraph_list[i] = "<p>" + paragraph_list[i] + "</p>"
        else:
            rmelements.append(i)
    for index in rmelements:
        del paragraph_list[index]

    return "".join(paragraph_list)


def RemParagraphElements(text):
    pass
