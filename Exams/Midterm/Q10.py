import re

str_lst1 = ["a1b2c3", "A5b9Z7q4", "C7u8D0", "e1e1e0", "5p6w"]
str_lst2 = ["aa34h8", "a5n8;9", "AAAAbbb", "123456"]
match_re = "(?:[a-zA-Z][0-9])+[a-zA-Z]?|(?:[0-9][a-zA-Z])+[0-9]?"

print("Testing Matching Strings...")
for test_str in str_lst1:
    print(re.findall(match_re, test_str))

print("Testing Non-matching Strings...")
for test_str in str_lst2:
    print(re.findall(match_re, test_str))
