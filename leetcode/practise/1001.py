class Solution:
    def gridIllumination(self, n: int, lamps, queries):
        xaxis = {}
        yaxis = {}
        yxaxis = {}
        nyxaxis = {}

        temp = set()

        for cop in lamps:
            # cop: list [x,y]
            if (cop[0], cop[1]) in temp:
                continue
            temp.add((cop[0], cop[1]))

            if cop[0] in xaxis:
                xaxis[cop[0]] += 1
            else:
                xaxis[cop[0]] = 1

            if cop[1] in yaxis:
                yaxis[cop[1]] += 1
            else:
                yaxis[cop[1]] = 1

            if cop[0] - cop[1] in yxaxis:
                yxaxis[cop[0] - cop[1]] += 1
            else:
                yxaxis[cop[0] - cop[1]] = 1

            if cop[0] + cop[1] in nyxaxis:
                nyxaxis[cop[0] + cop[1]] += 1
            else:
                nyxaxis[cop[0] + cop[1]] = 1


        def lighting(the_dict, value):
            if value not in the_dict:
                return False
            if the_dict[value] == 0:
                return False
            return True

        light = [0] * len(queries)
        for i, [row, col] in enumerate(queries):
            # lighting or not
            if lighting(xaxis, row) or lighting(yaxis, col) or lighting(yxaxis, row - col) or lighting(nyxaxis, row + col):
                light[i] = 1
            else:
                light[i] = 0
            # close the lamps in 3*3
            for r in range(row - 1, row + 2):
                for c in range(col - 1, col + 2):
                    if r < 0 or c < 0 or r > n or c > n or (r, c) not in temp:
                        continue
                    temp.remove((r, c))
                    xaxis[r] -= 1
                    yaxis[c] -= 1
                    yxaxis[r - c] -= 1
                    nyxaxis[r + c] -= 1
        return light

