students=[]
scores=[]

n=int(input("enter the number of students"))

for i in range(n):
    student_name=input("enter the name of the student:")
    student_score=input("enter the score of the student:")
    students.append(student_name)
    scores.append(int(student_score))


    total_score =sum(scores)
    average_score=total_score/n

    print("average score:",average_score)
    
print("\nstudent grade report:")
print("-----------------------")
print(" scores:", scores)
print(" students:", students)

for j, k in zip(students, scores):
    if k >=80:
        print('Hello', j, 'You have achieved A grade, with the scrore of', k)
        
    elif k >=60:
        print('Hello', j, 'You have achieved B grade, with the score of', k)
    elif k >=40:
        print('Hello', j, 'You have achieved C grade, with the score of', k)
    else:
        print('Hello', j, 'You have achieved F grade, with the score of', k)


