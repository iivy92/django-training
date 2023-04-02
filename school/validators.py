def valid_document_number(document_number):
    return len(document_number) != 11

def valid_name(name):
    name = name.replace(" ", "")
    return name.isalpha()