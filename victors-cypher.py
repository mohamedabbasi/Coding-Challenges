def decypher(sentence):
    result = []
    final = []
    cypher = sentence.split()
    # .split() is a built in function that appends all word in a string
    # to different elements in a list (to make it easir to loop through)
    # Ex: "Have a good day" becomes => ['Have', 'a', 'good', 'day']
    for i in cypher:
        # Now we can loop through each word one by one to decypher them
        result.append(f"{chr(int(i[0:3]))}{i[3:]}") if i[0:3].isdigit() else result.append(f"{chr(int(i[0:2]))}{i[2:]}")
        # 'chr' is also a built in function that changes an integer and swaps it to it's ASCII letter
        # Ex: 66 becomes 'b'
    # The list I made 'result' changed every ASCII number and matched it to it's letter
    # print(result) to see what it looks like
    for x in result:
        final.append(f"{x[0]}{x[-1]}{x[2:-1]}{x[1]}") if len(x) > 2 else final.append(x)
        # Here I'm just swapping the second letter with the last letter
    return " ".join(final)

print(decypher("66eaml 77dhameo 105f 121uo 104dtea 116sih 112mobler"))
