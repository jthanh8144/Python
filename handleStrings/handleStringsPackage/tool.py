import sys
import readFile

def main():
    strUsage = 'Usage: tool.py path_to_text_file [-lw | -cw | -cs | -f | -ot ]'
    if len(sys.argv) == 2:
        readFile.main(sys.argv[1])
    elif len(sys.argv) == 3:
        data = readFile.readFile(sys.argv[1])
        match sys.argv[2]:
            case '-lw':
                print('Danh sach cac tu xuat hien trong file:\n', readFile.getListWord(data))
            case '-cw':
                print('So tu:', len(readFile.getListWord(data)))
            case '-cs':
                print('So cau:', readFile.countSentence(data))
            case '-f':
                print('Tan suat xuat hien cua cac tu trong file:\n', readFile.freqWord(data))
            case '-ot':
                print('Cac tu xuat hien 1 lan trong file:\n', readFile.wordAppearedOnce(data))
    else:
        sys.exit(strUsage)

if __name__ == "__main__":
    main()
