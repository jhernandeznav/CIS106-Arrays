def display_parallel(last_name, exam_scores):
    for index in range(len(last_name)):
        print(last_name[index] + " exam score is " + str(exam_scores[index]))


def main():
    last_name = ["Cielo", "Combs", "Cooper", "Dawson", "Gardner", "Holland", "Nava", "Powers", "Smith", "Wilson"]
    exam_scores = [80, 85, 75, 70, 82, 87, 90, 96, 92, 77]
    display_parallel(last_name, exam_scores)


main()
