
def reverseWords( s: str) -> str:
    words = s.split(' ')

    for i in range(len(words)):
        words[i] = words[i][::-1]

    return " ".join(words)
print(reverseWords("Let's take LeetCode contest")) # => "s'teL ekat edoCteeL tsetnoc"

print(reverseWords("God Ding")) # => "doG gniD"