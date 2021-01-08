def encryptRailFence(text, key):
    #   key is the number of rails (i.e lists to be created)
    #   key must be integer value
    base_num = key * 2 - 2
    output = ""

    for rail in range(key):
        first_jump, second_jump = base_num - (rail * 2), rail * 2
        index = rail
        output += text[index]

        while index < len(text):
            if first_jump != 0:
                index += first_jump
                if index < len(text):
                    output += text[index]
            if second_jump != 0:
                index += second_jump
                if index < len(text):
                    output += text[index]

    return output

# 1. Determine and calculate number of characters for each row
# 2. Create a list that shows info about how many characters are in each row (e.g. [3, 5, 2] shows that there is 3 characters in row 1, etc.)*
# 3. Read the created list to split the ciphertext into their individual rows (e.g. [["aaa"], ["bbbbb"], ["cc"]])
# 4. Go back and forth (zigzag) from each individual rows and take out the first character*
# *Suggestion a counter that counts back and forth based on boundary given (e.g. if given a tuple like (0, 3), it will count 0, 1, 2, 3, 2, 1, 0, 1..., note: it is not a seperate function, just a variable that store the tuple will do)


def decryptRailFence(text, key):
    text_length = len(text)
    #     calculating units
    unit = text_length // (key + key - 2)

    num_of_char_top = unit
    num_of_char_bottom = unit
    num_of_char_mid = unit*2

    list_of_segments = [num_of_char_top]
    for x in range(1, key-1):
        list_of_segments.append(num_of_char_mid)
    list_of_segments.append(num_of_char_bottom)
    # print(list_of_segments)

    list_text = []
    number_of_chars_in_one_V = key*2-2
    number_of_Vs = text_length // number_of_chars_in_one_V

    remaining_char = text_length - (number_of_chars_in_one_V*number_of_Vs)
    # print(remaining_char)

    boundary = [0, key - 1]
    count = 0
    boundary_reached = False
    while remaining_char > 0:
        list_of_segments[count] += 1
        remaining_char -= 1
        if not boundary_reached:
            count += 1
        else:
            count -= 1
        if count in boundary:
            boundary_reached = not boundary_reached

    # print('new {}' .format(list_of_segments))

    start = 0
    for r in range(key):
        list_text.append(text[start:start + list_of_segments[r]])
        # print(r, start, start+list_of_segments[r])
        start += list_of_segments[r]
    # print(list_text)
    # [["G", "G"],
    #  ["e", "r", "e"],
    #  ["e", "o", "e"],
    #  ["k", "f", "k"],
    #  ["s", "s"]]
    boundary = [0, key-1]
    count = 0
    boundary_reached = False
    output = ""
    complete_word = []
    for word in list_text:
        word_in_list = list(word)
        complete_word.append(word_in_list)
        # print(complete_word)

    while len(output) < text_length:
        output += complete_word[count].pop(0)
        # print(output)
        if not boundary_reached:
            count += 1
        else:
            count -= 1
        if count in boundary:
            boundary_reached = not boundary_reached
    return output


# print(encryptRailFence("GeeksforGeeks", 5))
# print(decryptRailFence("GGereeoekfkss", 5))

# "abcafghi"
#  a   b
#   x x x x
#    x   x

# 1       5           4     index = 4, len = 5
#   2   4             2
#     3               4
#
# 1       3     1       2
#   5   4         3   4
#     2             5
#
# 1   3   5           2   1   5   4    1   4   2    1    2   3
#   2   4             2     3   2        5   3        4    5
#
# 1           7            6, 0      0   6 - (0 * 2), 0 * 2
#   2       6   8          4, 2      1   6 - (1 * 2), 1 * 2
#     3   5       9        2, 4      2   6 - (2 * 2), 2 * 2
#       4           10     0, 6      3   6 - (3 * 2), 3 * 2

# 1               9                 8
#   2           8   10              6, 2
#     3       7        11           4, 4
#       4   6             12        2, 6
#         5                  13     0, 8


#
# print(encryptRailFence("GeeksforGeeks ", 3))
# print(decryptRailFence("GsGsekfrek eoe", 3))

#5 x1        x      x        x   x
#9  x2 x4      x x    x x      x x x
#4   x3        x      x        x
#

