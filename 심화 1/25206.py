# 전공 평점 = (학점 x 과목평점)의 합 / 학점의 총합

grade = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F'] # 학점
score = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0] # 과목평점

gradeXscore = 0
total_score = 0

for i in range(20):
    n, s, g = input().split()
    s = float(s)
    
    if(g != 'P'):
        gradeXscore += s * score[grade.index(g)]
        total_score += s

avg = gradeXscore / total_score

print(format(avg, '.6f'))

