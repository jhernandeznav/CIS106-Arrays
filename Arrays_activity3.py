def display_parallel(last_name, exam_scores):
    for index in range(len(last_name)):
        print(last_name[index] + " exam score is " + str(exam_scores[index]))


def max(exam_score):
    maximum = exam_score[0]
    for index in range(1, len(exam_score)):
        if maximum < exam_score[index]:
            maximum = exam_score[index]
    return maximum


def min(exam_score):
    minimum = exam_score[0]
    for index in range(1, len(exam_score)):
        if minimum > exam_score[index]:
            minimum = exam_score[index]
    return minimum


def main():
    last_name = ["Cielo", "Combs", "Cooper", "Dawson", "Gardner", "Holland", "Nava", "Powers", "Smith", "Wilson"]
    exam_scores = [80, 85, 75, 70, 82, 87, 90, 96, 92, 77]
    display_parallel(last_name, exam_scores)
    average = sum(exam_scores) / 10
    maximum = max(exam_scores)
    minimum = min(exam_scores)
    print("Maximum score: " + str(maximum))
    print("Minimum score: " + str(minimum))
    print("Average test score: ", average)


main()
