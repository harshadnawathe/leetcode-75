class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rads, dirs = [], []
        for i, senator in enumerate(senate):
            if senator == "R":
                rads.append(i)
            else:
                dirs.append(i)

        r = d = 0
        n = len(senate)
        while r < len(rads) and d < len(dirs):
            if rads[r] < dirs[d]:
                rads.append(n)
            else:
                dirs.append(n)

            n += 1
            r += 1
            d += 1

        return "Radiant" if r < len(rads) else "Dire"
