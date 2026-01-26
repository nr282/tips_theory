"""
Given a string s, reverse only all the vowels in the string and return it.


The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in
both lower and upper cases, more than once.


Example 1:

    TEABR ----> TAEBR

    vowel idx = [1,2]


    A

"""

def reverseVowels(s: str) -> str:

    vowels = ['a', 'e', 'i', 'o', 'u']
    letters = [letter for letter in s]
    vowel_idx = []
    for idx, letter in enumerate(letters):
        if letter.lower() in vowels:
            vowel_idx.append(idx)

    n = len(vowel_idx)
    for j in range(n//2):
        left_idx = vowel_idx[j]
        right_idx = vowel_idx[n-j-1]
        letter_left = letters[left_idx]
        letter_right = letters[right_idx]
        letters[left_idx] = letter_right
        letters[right_idx] = letter_left

    return "".join(letters)


if __name__ == "__main__":

    s = "teabrat"
    res = reverseVowels(s)