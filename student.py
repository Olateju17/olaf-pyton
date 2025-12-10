student_data= {'id1 ' :
{'name' :['Sara'],'class': ['V'],'subject_intergretion':['english,maths,science']}},
'id2':
{'name' :['Sara'],'class':['V'], 'subject_intergretion':['english,maths,science']}

'id3':
{'name' :['Surya'],'class':['V'], 'subject_intergretion':['english,maths,science']},

result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key] = value
print(result)