numberOfScores = score = total = scoreCount = 0
average = 0.0
numberOfScores = int(input("Please enter the number of scores you would like to average: "))

score = int(input("Please enter a score: "))
total += score
scoreCount += 1

average = total / numberOfScores
print(average)
