def course_grader(test_scores):
    # Your code here
    # calculate average
    #average = statistics.mean(float(test_scores))
    sum_of_scores = sum(test_scores)
    count_of_scores = len(test_scores)
    average = sum_of_scores/count_of_scores
    minimum = min(test_scores)
    # if average score is >= 70 AND no score is below 50, pass
    if average >= 70 and minimum > 50:
        return "Pass"
    # if average score < 70 OR at least one score is below 50, fail
    elif average < 70 or minimum < 50:
        return "Fail"

def main():
    print(course_grader([100,75,45]))     # "fail"
    print(course_grader([100,70,85]))     # "pass"
    print(course_grader([80,60,60]))      # "fail"
    print(course_grader([80,80,90,30,80]))  # "fail"
    print(course_grader([70,70,70,70,70]))  # "pass"
    print(course_grader([60,80,80,70,70]))  # "pass"

if __name__ == "__main__":
    main()
