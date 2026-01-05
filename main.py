from pyscript import display, document

def calculate(k):
 
    first = document.getElementById("fname").value
    last = document.getElementById("lname").value

    scigrade = document.getElementById("scigrade").value
    mathgrade = document.getElementById("mathgrade").value
    ictgrade = document.getElementById("ictgrade").value
    enggrade = document.getElementById("enggrade").value
    filgrade = document.getElementById("filgrade").value
    vegrade = document.getElementById("vegrade").value


    # unpacking
    subjects = ["Science", "Math", "ICT", "English", "Filipino", "VE"]
    units = (5, 5, 2, 5, 3, 1)
    science, math, ict, eng, fil, ve = subjects
    unit1, unit2, unit3, unit4, unit5, unit6= units

    #calculations
    sciave = int(scigrade) * unit1
    mathave = int(mathgrade) * unit2
    ictave = int(ictgrade) * unit3
    enggave = int(enggrade) * unit4 
    filave = int(filgrade) * unit5
    veave = int(vegrade) * unit6
    num_of_units = unit1 + unit2 + unit3 + unit4 + unit5 + unit6
    gwa = round((sciave + mathave + ictave + enggave + filave + veave) / num_of_units, 2) 

    if gwa > 74:
        outcome = 'PASSED'
    else:
        outcome = 'FAILED'

    # displays
    document.getElementById('output').innerHTML = ' '
    display(f"Student Name: {first} {last}", target="output")
    display(f"Subject Grades:", target="output")
    display(f"{subjects[0]} = {scigrade}", target='output')
    display(f"{subjects[1]} = {mathgrade}", target='output')
    display(f"{subjects[2]} = {ictgrade}", target='output')
    display(f"{subjects[3]} = {enggrade}", target='output')
    display(f"{subjects[4]} = {filgrade}", target='output')
    display(f"{subjects[5]} = {vegrade}", target='output')
    display(f"General Weighted Average: {gwa}", target="output")
    display(f'You have {outcome} this quarter.', target='outcome')