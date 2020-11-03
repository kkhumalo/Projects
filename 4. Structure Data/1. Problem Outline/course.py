

def create_outline():
    #step1
    course_topics = ['Introduction to Python','Tools of the Trade','How to make decisions','How to repeat code','How to structure data','Functions','Modules']
    print('Course Topics:')
    course_topics.sort()
    for course in course_topics:
        print("* "+course)
    print('Problems:')

    #step2
    problems = ['Problem 1, ', 'Problem 2, ', 'Problem 3']
    for problem_list in course_topics:
        print("* "+ problem_list ,": " , end="" )
        for i in problems:
            print(i, end="")
        print()    

    #step3
    print('Student Progress: ')
    students = ['Kamogelo', 'Mbali', 'Thembi', 'John', 'Sam']
    status = ['[STARTED]', '[GRADED]', '[COMPLETED]']
    count = 0
    status.sort(reverse = True)

    for i in status:
        print(f"{count+1}. {students[count]} - {course_topics[count]} - {problems[count]} - {status[count]}")
        count += 1
    print()

if __name__ == "__main__":
    create_outline()
