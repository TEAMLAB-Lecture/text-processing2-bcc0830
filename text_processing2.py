#######################
# Test Processing II  #
#######################


def digits_to_words(input_string):
    res = {'0' : 'zero' , '1' : 'one', '2' : 'two', '3' : 'three', '4' : 'four', '5' : 'five', '6' : 'six', '7' : 'seven',
           '8' : 'eight', '9' : 'nine'}
    digit_string = []
    for i in input_string:
        if i.isdigit():
            digit_string.append(res[i])
    return ' '.join(digit_string)


"""
컴퓨터 프로그래밍에 많은 명명 규칙이 있지만, 두 규칙이 특히 흔히 쓰입니다. 
첫번째로는, 변수 이름을 'underscore'로 나눠준다거나, (ex. under_score_variable)
두번째로는, 변수 이름을 대소문자 구별해 구분자 (delimiter)없이 쓰는 경우가 있습니다. 
이 두번째의 경우에는 첫번째 단어는 소문자로, 그 후에 오는 단어들의 첫번째 글자들은 대문자로 쓰입니다 (ex. camelCaseVariable). 
"""


def to_camel_case(underscore_str):
    res = underscore_str.split('_')
    camelcase_str = ''
    for i in range(len(res)):
        if i == 0:
            camelcase_str += res[i]
        else:
            camelcase_str += res[i].captialize()

    return camelcase_str
