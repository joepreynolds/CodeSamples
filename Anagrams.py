
def group_anagrams(words: list[str]) -> list[list[str]]:
    anagram_signatures = []
    for word in words:
        split = list(word)
        split.sort()
        if split not in anagram_signatures:
            anagram_signatures.append(split)

    wordsListlist = []
    for anagram_signature in anagram_signatures:
        wordsList = []
        for word in words:
            split = list(word)
            split.sort()
            if split == anagram_signature:
                wordsList.append(word)
        wordsListlist.append(wordsList)

    return wordsListlist


words = ["eat", "tea", "tan", "ate", "nat", "bat", "tab", "net", "dome", "mode", "odem"]
result = group_anagrams(words)
print("The Result is: ", result)
