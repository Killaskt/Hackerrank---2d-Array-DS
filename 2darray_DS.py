# Hackerrank Coding Challenge 
# 2D Array - DS
# Challenge Link
# https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

test1 = [
    [ 0, -4, -6, 0 ,-7 ,-6],
    [-1, -2, -6, -8, -3, -1],
    [-8, -4, -2, -8, -8, -6],
    [-3, -1, -2, -5, -7, -4],
    [-3, -5, -3, -6, -6, -6],
    [-3, -6,  0,-8 ,-6 ,-7]
]

# Complete the hourglassSum function below.
def hourglassSum(arr):
    hourglass_sums = []
    row = 0
    i = 0

    while i < 4 and len(hourglass_sums) < 16:
        top = sum(arr[row][i:i+3])
        mid = arr[row+1][i+1]
        bot = sum(arr[row+2][i:i+3])
        curr = top + mid + bot
        print ('hourglass ({},{}) sum: {}'.format(row, i, curr))
        hourglass_sums.append(curr)
        if row == 0 and i == 0:
            max_sum = curr
        elif curr > max_sum : 
            max_sum = curr
        i += 1

        if (len(hourglass_sums) % 4 == 0): 
            i = 0
            row += 1

    return max_sum

print(hourglassSum(test1))