from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        intervalHeights = list()
        maxHeight = height[0]
        volume = 0
        length = 0

        for heights in height:
            if int(heights) >= maxHeight:
                volume += length * maxHeight - sum(intervalHeights)
                print("heights ", heights)
                print("volume ", volume)
                print("maxHeight ", maxHeight)

                maxHeight = heights
                intervalHeights.clear()
                length = 0
            else:
                intervalHeights.append(heights)
                length += 1
        if len(intervalHeights) != 0:
            intervalHeights = intervalHeights[::-1]
            invervalMaxHeight = intervalHeights[0]
            length = 0
            innerIntervalHeights = list()
            for heights in intervalHeights:
                if int(heights) >= invervalMaxHeight:
                    volume += length * invervalMaxHeight - sum(innerIntervalHeights)
                    print("M heights ", heights)
                    print("M volume ", volume)
                    print("M maxHeight ", invervalMaxHeight)

                    invervalMaxHeight = heights
                    innerIntervalHeights.clear()
                    length = 0
                else:
                    innerIntervalHeights.append(heights)
                    length += 1
            if len(innerIntervalHeights) != 0:
                if maxHeight >= invervalMaxHeight:
                    volume += length * invervalMaxHeight - sum(innerIntervalHeights)
                    print("M2 heights ", heights)
                    print("M2 volume ", volume)
                    print("M2 maxHeight ", invervalMaxHeight)
                    innerIntervalHeights.clear()
                    length = 0


        print(volume)
        print("Max Height ", maxHeight)
        print("Length ", length)
        print(intervalHeights)
        return volume

if __name__ == "__main__":
    Solution.trap(self=Solution(),height=[10, 4, 5, 4, 5, 0, 5, 2, 1, 30, 2, 1, 4, 2, 3, 4, 3])
