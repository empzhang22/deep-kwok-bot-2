# tutorial: https://blog.enterprisedna.co/python-write-to-file/
messages = ["bozo", "rip", "goofy", "ahh", "yapper"]

# Method 1: Write using a list of strings
# file = open('test.txt', 'w')
# file.writelines(messages)
# file.close()

# Method 2: Write individual messages
# file = open('test.txt', 'w')
# for message in messages:
#     file.write(message + '\n')
# file.close()

# Removing all newline characters
clean = open('test.txt').read().replace('\n', ' ')