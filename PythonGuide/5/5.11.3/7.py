empy = {}
science = {
    'physics' : ['nuclear physics', 'optics', 'thermodynamics'],
    'computer science' : empy,
    'biology' : empy
    }
subjects = {
    'science' : science,
    'humanities' : empy,
    'public' : empy
    }

print(subjects['science'], subjects['science']['physics'])
