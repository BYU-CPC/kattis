for _ in range(int(input())):
    name, study, birth, courses = input().split()
    sYear = int(study.split('/')[0])
    bYear = int(birth.split('/')[0])
    courses = int(courses)

    status = ''
    if sYear >= 2010:
        status = 'eligible'
    elif bYear >= 1991:
        status = 'eligible'
    elif courses >= 41:
        status = 'ineligible'
    else:
        status = 'coach petitions'
    print(name, status)