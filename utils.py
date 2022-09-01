from random import Random


def getRandGenChars(size: int = 8) -> str:
    result = ""
    random = Random()
    for i in range(size):
        result += chr(random.randint(65,90))
    return result

def writeToFile(fileName: str, text: str) -> None:
    newFile = open("out/"+fileName, "w")
    newFile.write(text)
    newFile.close()

if __name__ == "__main__":
    print(getRandGenChars())