class Solution:

    res = []

    letterMap = {
        "0": " ",
        "1": "",
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def letterCombinations(self, digits: str):
        self.res = []
        if digits == "":
            return self.res
        self.findCombination(digits, 0, "")
        return self.res

    def findCombination(self, digits: str, index: int, s: str):
        if index == len(digits):
            self.res.append(s)
            return
        num = digits[index]
        letters = self.letterMap[num]
        for l in letters:
            self.findCombination(digits, index + 1, s + l)

        return


def input_data(file_name):
    with open(file_name, 'r') as data:
        buttons_seq = data.readline().strip()
    s = Solution()
    result=s.letterCombinations(buttons_seq)
    print(*result)


if __name__ == '__main__':
    input_data('input.txt')
