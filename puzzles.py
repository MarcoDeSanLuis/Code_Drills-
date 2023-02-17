# find common characters --------------------

def find_common_chars(word1, word2):
  char_list1 = list(word1.lower())
  char_list2 = list(word2.lower())
  common_chars = []

  for c in char_list2:
    if c in char_list1 and c not in common_chars:
      common_chars.append(c)

  print(f'Common characters: {", ".join(common_chars)}')

find_common_chars('apple', 'pear')

# find most common characters --------------------

def find_most_common_chars(sent):
  most_common_chars = []
  char_list = list(sent.lower())
  char_map = {}
  max_freq = 0

  for c in char_list:
    if c in char_map:
      char_map[c] += 1
    else:
      char_map[c] = 1

  for c in char_map:
    if char_map[c] > max_freq:
      max_freq = char_map[c]
    
  for c in char_map:
    if char_map[c] == max_freq:
      most_common_chars.append(c)

  print(f'Most common characters: {", ".join(most_common_chars)} | occurences: {max_freq}')

find_most_common_chars('Yabba, dabba, doooooo!!')

# shift array left -----------------------------------------------------------------

my_nums = [1, 2, 3, 4, 5]

def shift_left(num_list, rotations):
  i = 0
  
  while i < rotations:
    moved_num = num_list.pop(0)
    num_list.append(moved_num)
    i += 1

  print(num_list)

shift_left(my_nums, 2)
