import os.path as op
def main():
    for i in  range (0,1000):
        if (i<10):
            fileName = "data00" + str(i) + ".txt"
        if (i >= 10) and (i<100):
            fileName = "data0" + str(i) + ".txt"
        if  (i >= 100):
            fileName = "data" + str(i) + ".txt"

        if op.exists(fileName):
            file = open(fileName, 'r' )
            #print(file.readline().split(' '))
            for line in file:
                Data = []
                Data = line.split(' ')
                if (Data[1])
                print(Data)


if __name__ == "__main__":
            main()