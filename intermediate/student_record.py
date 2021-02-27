import operator
from os import read

def read_student_details():
    print()
    print('Enter the number of students: ')

    a = int(input())
    student_record = {}

    for student in range(0, a):
        print('Enter the name of the student: ')
        name = input()

        print('Enter the marks of the student: ')
        marks = int(input())
        student_record[name] = marks
    print()
    return student_record


def rank_students(student_record):
    try:
        print()
        sortedstudent_record = sorted(student_record.items(), key = operator.itemgetter(1), reverse = True) 
        print(sortedstudent_record)

        print('{} has secured First rank, scoring {} marks'.format(sortedstudent_record[0][0], sortedstudent_record[0][1]))
        print('{} has secured Second rank, scoring {} marks'.format(sortedstudent_record[1][0], sortedstudent_record[1][1]))
        print('{} has secured Third rank, scoring {} marks'.format(sortedstudent_record[2][0], sortedstudent_record[2][1]))
        print()
        return sortedstudent_record

    except IndexError:
      print('Enter a minimun of 3 Students')
      quit()


def reward_students(sortedstudent_record, reward):
    print()

    print('{} Is going to be rewared with $ {}, cash'.format(sortedstudent_record[0][0], reward[0]))
    print('{} Is going to be rewared with $ {}, cash'.format(sortedstudent_record[1][0], reward[1]))
    print('{} Is going to be rewared with $ {}, cash'.format(sortedstudent_record[2][0], reward[2]))


def appeciate_students(sortedstudent_record):
    print()

    for record in sortedstudent_record:
        if record[1] >= 480:
            print('Congratulations on scoring {} marks, {}'.format(record[1], record[0]))
        else:
            break
    print()

if __name__ == '__main__':

    student_record= read_student_details()
    sortedstudent_record = rank_students(student_record)
    reward = (500, 300, 100)
    reward_students(sortedstudent_record, reward)
    appeciate_students(sortedstudent_record)