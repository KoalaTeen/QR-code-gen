<<<<<<< HEAD
def usesleft():
    text = open(r'uses.txt', 'r')
    read_value = text.readline(4)
    text.close()
    # Retracts the value with 1
    int_read_value = int(read_value)
    str_read_value = str(int_read_value)
    int_replace_text = int_read_value - 1
    str_replace_text = str(int_replace_text)
    with open(r'uses.txt', 'r') as file:
        data = file.read()
        # If total uses is 0 replace it with another 9999
        if data == str(0):
            data = data.replace(str_read_value, str(9999))
        else:
            data = data.replace(str_read_value, str_replace_text)
    with open(r'uses.txt', 'w') as file:
        file.write(data)
    print(str_replace_text + ' uses left.')
    uses = str_replace_text
    return uses
=======
def usesleft():
    text = open(r'uses.txt', 'r')
    read_value = text.readline(4)
    text.close()
    # Retracts the value with 1
    int_read_value = int(read_value)
    str_read_value = str(int_read_value)
    int_replace_text = int_read_value - 1
    str_replace_text = str(int_replace_text)
    with open(r'uses.txt', 'r') as file:
        data = file.read()
        # If total uses is 0 replace it with another 9999
        if data == str(0):
            data = data.replace(str_read_value, str(9999))
        else:
            data = data.replace(str_read_value, str_replace_text)
    with open(r'uses.txt', 'w') as file:
        file.write(data)
    print(str_replace_text + ' uses left.')
    uses = str_replace_text
    return uses
>>>>>>> ec58f8cda52865816fd5d8177f34b0bd8f33384e
