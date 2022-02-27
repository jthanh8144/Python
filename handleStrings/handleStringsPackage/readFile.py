from typing import Counter

__PUNCTUATION__ = '?!.,'

def readFile(path):
    file = open(path, 'r', encoding='utf-8')
    data = file.read().strip().replace('\n', ' ').lower()
    return data

def getListWord(data):
    listWord = data.split(' ')
    for i in range(len(listWord)):
        while listWord[i][-1] in __PUNCTUATION__:
            listWord[i] = listWord[i][:-1]
    return listWord

def countSentence(data):
    sentence = 0
    for character in data:
        if character in __PUNCTUATION__[:-1]:
            sentence = sentence + 1

def freqWord(data):
    listWord = getListWord(data)
    listCount = dict(Counter(listWord))
    return listCount

def wordAppearedOnce(data):
    listCount = freqWord(data)
    word1Time = dict(filter(lambda e: e[1] == 1, listCount.items()))
    return word1Time


def main(path):
    data = readFile(path)
    listWord = getListWord(data)
    print('Danh sach cac tu xuat hien trong file:\n', listWord)
    print('So tu:', len(listWord))
    sentence = countSentence(data)
    print('So cau:', sentence)
    listCount = freqWord(data)
    print('Tan suat xuat hien cua cac tu trong file:\n', listCount)
    word1Time = wordAppearedOnce(data)
    print('Cac tu xuat hien 1 lan trong file:\n', word1Time)

# if __name__ == "__main__":
#     main('..\inp.txt')
