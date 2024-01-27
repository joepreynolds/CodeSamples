emojis = {
    ":)": "😀",
    "8)": "😎",
    ":(": "☹️",
    ";P": "😜",
    ":O": "😮",
    "<3": "❤️",
    "<>": "💋",
    "(P)": "💩",
    "(C)": "😺",
    "O:)": "😇"
}


def show_emojis():
    print(emoji_converter("""
-help- for commands
-quit- to exit
-learn- to teach me a new emoji
or 
-type a message.  (C) Feel free to use Emojis, if the message contains any :-| emojis I will 
     try to <3 convert them to an image :-) here are the emojis i know:"""))

    print("-" * 20)
    for emoji in emojis:
        if len(emoji) == 2:
            print(f"|   {emoji}  |  {emojis.get(emoji)}      |")
        else:
            print(f"|  {emoji}  |  {emojis.get(emoji)}      |")
    print("-" * 20)


def emoji_converter(message):
    words = message.split(" ")
    output = ""
    for word in words:
        output += emojis.get(word.upper().replace("-", ""), word) + " "
    return output


print("Type your message or type help for more information:")

message = input(">")
#message = "help"
while message.upper() != "QUIT":
    if message.upper() == "HELP":
        show_emojis()
        message = input(">")
    elif message.upper() == "LEARN":
        print("Teach me.... ")
        chars = input("What is the character representation of the emoji: ")
        img = input("What is the image representation of the emoji:")
        emojis[chars.upper().replace("-", "")] = img
        message = input(">")

    else:
        print(emoji_converter(message))
        message = input(">")
