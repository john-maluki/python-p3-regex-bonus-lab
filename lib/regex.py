import re

my_pattern = r"[^\s].*today.*"
my_regex = re.compile(my_pattern, re.MULTILINE)

# FINDALL_STRING = """
#     It's such a lovely day today.
#     Where'd all the time go?
#     Some weather we're having today, huh?
#     Tomorrow never knows!
#     Maybe today's just not my day.
#     It's clobbering time!
# """

# print(my_regex.findall(FINDALL_STRING))