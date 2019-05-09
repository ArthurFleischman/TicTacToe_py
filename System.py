map = ([' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '])


class Game():

    def printmap(self, map):
        print('  0 1 2')
        for y in range(3):
            print(f'{y}|', end='')
            for x in range(3):
                print(f'{map[y][x]}', end='|')
            print('\n', end='')

    def testline(self, map):
        for line in range(3):
            if map[line] == ['x', 'x', 'x']:
                print('X win')
                return True
            elif map[line] == ['o', 'o', 'o']:
                print('O win')
                return True
        return False

    def testdia(self, map):
        pass

    def testcol(self, map):

        contx = 0
        conto = 0

        for line in range(3):
            for col in range(3):
                if map[col][line::3][0] == 'x':
                    contx += 1
                elif map[col][line::3][0] == 'o':
                    conto += 1
                if contx == 3:
                    print('X win')
                    return True
                elif conto == 3:
                    print('O win')
                    return True
                else:
                    return False
            contx = 0
            conto = 0


def main():
    game = Game()
    vez = 0
    posx = -1
    posy = -1
    while 1:
        game.printmap(map)
        if game.testline(map) or game.testdia(map) or game.testcol(map):
            break
        try:
            posx = int(input("digite a linha\n"))
            posy = int(input(" digite a coluna\n"))
        except:
            print('digite uma linha/coluna válida')
        else:
            if (posx > 2 or posy > 2) or map[posx][posy] != ' ':
                print('\n#digite uma linha/coluna válida#\n')
                continue
            else:
                while 1:
                    if vez == 0:
                        map[posx][posy] = 'x'
                        vez = 1
                        break
                    else:
                        map[posx][posy] = 'o'
                        vez = 0
                        break


if __name__ == "__main__":
    main()
