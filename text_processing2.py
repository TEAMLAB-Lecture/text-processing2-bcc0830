#######################
# Test Processing II  #
#######################


def digits_to_words(input_string):
    res = {'0' : 'zero', '1' : 'one', '2' : 'two', '3' : 'three', '4' : 'four', '5' : 'five', '6' : 'six', '7' : 'seven',
           '8' : 'eight', '9' : 'nine'}
    digit_string = []
    for i in input_string:
        if i.isdigit():
            digit_string.append(res[i])
    return ' '.join(digit_string)

def to_camel_case(underscore_str):
    res = underscore_str.split('_')
    camelcase_str = ''
    for i in range(len(res)):
        if i == 0:
            camelcase_str += res[i]
        else:
            camelcase_str += res[i].capitalize()
    return camelcase_str
