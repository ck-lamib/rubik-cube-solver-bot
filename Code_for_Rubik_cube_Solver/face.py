# ####### The cube on the facelet level is described by positions of the colored stickers. #############################

from defs import cornerFacelet, edgeFacelet, cornerColor, edgeColor
from enums import Color, Corner, Edge
import cubie


class FaceCube:
    """Represent a cube on the facelet level with 54 colored facelets."""
    def __init__(self):
        self.f = []
        for i in range(9):
            self.f.append(Color.W)
        for i in range(9):
            self.f.append(Color.R)
        for i in range(9):
            self.f.append(Color.G)
        for i in range(9):
            self.f.append(Color.Y)
        for i in range(9):
            self.f.append(Color.O)
        for i in range(9):
            self.f.append(Color.B)

    def __str__(self):
        return self.to_string()

# Construct a facelet cube from a inserted cubeconfig and check for validation
    def from_string(self, s):
        if len(s) < 54:
            return 'Input cubeconfig (' + s + ') contains less than requrired facelets(<54).'
        elif len(s) > 54:
            return 'Input cubeconfig (' + s + ') contains more than requrired facelets(54<).'
        faceColorList = [0] * 6
        for i in range(54):
            if s[i] == 'W':
                self.f[i] = Color.W
                faceColorList[Color.W] += 1
            elif s[i] == 'R':
                self.f[i] = Color.R
                faceColorList[Color.R] += 1
            elif s[i] == 'G':
                self.f[i] = Color.G
                faceColorList[Color.G] += 1
            elif s[i] == 'Y':
                self.f[i] = Color.Y
                faceColorList[Color.Y] += 1
            elif s[i] == 'O':
                self.f[i] = Color.O
                faceColorList[Color.O] += 1
            elif s[i] == 'B':
                self.f[i] = Color.B
                faceColorList[Color.B] += 1

        if all(x == 9 for x in faceColorList):
            return True
        else:
            return 'Input cubeconfig (' + s + ') does not contain exactly 9 facelets of each color.'

    def to_string(self):
        """Give a string representation of the facelet cube."""
        s = ''
        for i in range(54):
            if self.f[i] == Color.W:
                s += 'W'
            elif self.f[i] == Color.R:
                s += 'R'
            elif self.f[i] == Color.G:
                s += 'G'
            elif self.f[i] == Color.Y:
                s += 'Y'
            elif self.f[i] == Color.O:
                s += 'O'
            elif self.f[i] == Color.B:
                s += 'B'
        return s

    def to_2dstring(self):
        """Give a 2dstring representation of a facelet cube."""
        s = self.to_string()
        r = '   ' + s[0:3] + '\n   ' + s[3:6] + '\n   ' + s[6:9] + '\n'
        r += s[36:39] + s[18:21] + s[9:12] + s[45:48] + '\n' + s[39:42] + s[21:24] + s[12:15] + s[48:51] \
            + '\n' + s[42:45] + s[24:27] + s[15:18] + s[51:54] + '\n'
        r += '   ' + s[27:30] + '\n   ' + s[30:33] + '\n   ' + s[33:36] + '\n'
        return r

    def to_cubie_cube(self):
        """Return a cubie representation of the facelet cube."""
        cc = cubie.CubieCube()
        cc.cp = [-1] * 8  # invalidate corner and edge permutation
        cc.ep = [-1] * 12
        for i in Corner:
            fac = cornerFacelet[i]  # facelets of corner  at position i
            ori = 0
            for ori in range(3):
                if self.f[fac[ori]] == Color.W or self.f[fac[ori]] == Color.Y:
                    break
            col1 = self.f[fac[(ori + 1) % 3]]  # colors which identify the corner at position i
            col2 = self.f[fac[(ori + 2) % 3]]
            for j in Corner:
                col = cornerColor[j]  # colors of corner j
                if col1 == col[1] and col2 == col[2]:
                    cc.cp[i] = j  # we have corner j in corner position i
                    cc.co[i] = ori
                    break

        for i in Edge:
            for j in Edge:
                if self.f[edgeFacelet[i][0]] == edgeColor[j][0] and \
                        self.f[edgeFacelet[i][1]] == edgeColor[j][1]:
                    cc.ep[i] = j
                    cc.eo[i] = 0
                    break
                if self.f[edgeFacelet[i][0]] == edgeColor[j][1] and \
                        self.f[edgeFacelet[i][1]] == edgeColor[j][0]:
                    cc.ep[i] = j
                    cc.eo[i] = 1
                    break
        return cc
