def max():
    stor=0
    markor=mindatabase.cursor()

    promp=("SELECT MAX(Studentnr) FROM Student")
    markor.execute(promp)
    for row in markor:
        stor=int(row[0])
