import sys
import getopt
from random import randint

input_file = "img.gif"


def glitchGif():
    with open(input_file, "rb") as imageFile:
        f = imageFile.read()
        b = bytearray(f)

    for x in range(0, sys.getsizeof(b)):
        if b[x] == 33:
            if b[x + 1] == 255:
                end = x
                break
            elif b[x + 1] == 249:
                end = x
                break

    print(end)

    for x in range(13, end):
        b[x] = randint(0, 255)

    with open('newGif.gif', 'wb') as f:
        f.write(b)
    print("DONE!")


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hi", ["inputFile="])
    except getopt.GetoptError:
        print('gifGlitcher.py -i <inputFile> ')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('gifGlitcher.py -i <inputFile>')
            sys.exit()
        elif (opt in ("-i", "--inputFile")):
            global input_file
            input_file = arg
    glitchGif()


if __name__ == '__main__':
    main(sys.argv[1:])
