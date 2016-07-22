def computeArea(A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        slen = 0
        swid = 0
        BigArea = (G - E)*(H - F) + (C - A)*(D - B)
        if A > G or C < E or B > H or D < F:
            return BigArea
        if A - E < 0 and G - C > 0:
            slen = C - E
        elif A - E < 0 and G - C < 0:
            slen = G - E
        elif A - E > 0 and G - C < 0:
            slen = G - A
        elif A - E >= 0 and G - C >= 0:
            slen = C - A

        if D - H > 0 and B - F > 0:
            swid = H - B
        elif D - H < 0 and B - F > 0:
            swid = D - B
        elif D - H < 0 and B - F < 0:
            swid = D - F
        elif D - H >= 0 and B - F <= 0:
            swid = H - F

        return BigArea - slen*swid

print(computeArea(-5, -3, 0, 0, -3, -3, 3, 3))