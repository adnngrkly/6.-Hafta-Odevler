tahta = [["___", "___", "___"],
["___", "___", "___"],
["___", "___", "___"]]
print("\n"*15)
for i in tahta:
    print("\t".expandtabs(30), *i, end="\n"*2)
kazanma_olcutleri = [[[0, 0], [1, 0], [2, 0]],
[[0, 1], [1, 1], [2, 1]],
[[0, 2], [1, 2], [2, 2]],
[[0, 0], [0, 1], [0, 2]],
[[1, 0], [1, 1], [1, 2]],
[[2, 0], [2, 1], [2, 2]],
[[0, 0], [1, 1], [2, 2]],
[[0, 2], [1, 1], [2, 0]]]

kazanma_olcutleri1 = [[[0, 0], [1, 0], [2, 0]],
[[0, 1], [1, 1], [2, 1]],
[[0, 2], [1, 2], [2, 2]],
[[0, 0], [0, 1], [0, 2]],
[[1, 0], [1, 1], [1, 2]],
[[2, 0], [2, 1], [2, 2]],
[[0, 0], [1, 1], [2, 2]],
[[0, 2], [1, 1], [2, 0]]]

pcdeger=[]
x_durumu = []
o_durumu = []
sira = 1
import random

while True:

    if sira % 2 != 0:
        isaret = "X".center(3)
        print("ISARET: {}\n".format(isaret))
        x = input("yukaridan asagiya [1, 2, 3]: ")
        y = input("soldan saga [1, 2, 3]: ")
        x = int(x) - 1
        y = int(y) - 1
        print("\n" * 5)
        if tahta[x][y] == "___":
            tahta[x][y] = isaret
            x_durumu += [[x, y]]
            sira += 1
            for i in tahta:
                print("\t".expandtabs(30), *i, end="\n" * 2)
            for i in kazanma_olcutleri1:
                o = [z for z in i if z in o_durumu]
                x = [z for z in i if z in x_durumu]
                if len(o) == len(i):
                    print("O KAZANDI!")
                    quit()
                if len(x) == len(i):
                    print("X KAZANDI!")
                    quit()
            continue
        else:
            print("\nORASI DOLU! TEKRAR DENEYIN\n")
            continue

    else:
        isaret = "O".center(3)
        print("ISARET: {}\n".format(isaret))
        pcdeger.clear()

        for i in kazanma_olcutleri:
            el = [z for z in i if z in o_durumu]

            if len(el)==2:
                for y in el:
                    i.remove(y)
                    continue
                l = i[0][0]
                m = i[0][1]
                if tahta[l][m] == "___":
                    tahta[l][m] = isaret
                    print(isaret)
                    sira += 1
                    o_durumu += [[l, m]]
                    for i in tahta:
                        print("\t".expandtabs(30), *i, end="\n" * 2)
                    for i in kazanma_olcutleri1:
                        o = [z for z in i if z in o_durumu]
                        x = [z for z in i if z in x_durumu]
                        if len(o) == len(i):
                            print("O KAZANDI!")
                            quit()
                        if len(x) == len(i):
                            print("X KAZANDI!")
                            quit()

        for i in kazanma_olcutleri:
            s = [z for z in i if z in x_durumu]
            if len(s)==2:
                for y in s:
                    i.remove(y)
                    continue
                l = i[0][0]
                m = i[0][1]
                if tahta[l][m] == "___":
                    tahta[l][m] = isaret
                    print(isaret)
                    sira += 1
                    o_durumu += [[l, m]]
                    for i in tahta:
                        print("\t".expandtabs(30), *i, end="\n" * 2)
                    for i in kazanma_olcutleri1:
                        o = [z for z in i if z in o_durumu]
                        x = [z for z in i if z in x_durumu]
                        if len(o) == len(i):
                            print("O KAZANDI!")
                            quit()
                        if len(x) == len(i):
                            print("X KAZANDI!")
                            quit()
                break
            else:
                continue
        if sira % 2 != 0:
            continue
        else:
            pass
        for i in x_durumu:
            for k in i:
                if k == 0:
                    pcdeger.append([0, 0])
                    pcdeger.append([0, 1])
                    pcdeger.append([0, 2])
                    pcdeger.append([1, 0])
                    pcdeger.append([2, 0])
                if k == 1:
                    pcdeger.append([1, 0])
                    pcdeger.append([1, 1])
                    pcdeger.append([1, 2])
                    pcdeger.append([2, 1])

                if k == 2:
                    pcdeger.append([2, 0])
                    pcdeger.append([2, 1])
                    pcdeger.append([1, 2])
                    pcdeger.append([0, 2])
        while True:
            isaret1 = random.choice(pcdeger)
            l = isaret1[0]
            m = isaret1[1]
            if tahta[l][m] == "___":
                tahta[l][m] = isaret
                print(isaret)
                sira += 1
                o_durumu += [[l, m]]
            for i in tahta:
                print("\t".expandtabs(30), *i, end="\n" * 2)
            for i in kazanma_olcutleri1:
                o = [z for z in i if z in o_durumu]
                x = [z for z in i if z in x_durumu]
                if len(o) == len(i):
                    print("O KAZANDI!")
                    quit()
                if len(x) == len(i):
                    print("X KAZANDI!")
                    quit()

            break
        continue

