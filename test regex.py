import re

regex_playlist = r"playlist\?list"

text = "https://www.youtube.com/watch?v=5qap5aO4i9A"

print(bool(re.search(regex, text)))