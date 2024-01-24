import re

pattern = re.compile(r'\d+')

# match_obj = pattern.match('123ab33c')
# print(match_obj.group()) if match_obj else print("No match")

# print(pattern.search('a44b33c').group())

# matches = re.findall(r'\d+', 'abc123xyz456')
# print(matches)
match_iter = re.finditer(r'\d+', 'abc123xyz456')
# for match in match_iter:
#     print(match.group())
# print([match.group() for match in match_iter])

# match_obj = re.match(r'(\d+)(\w+)', '123abc')
# all_groups = match_obj.groups()
# print(all_groups)
