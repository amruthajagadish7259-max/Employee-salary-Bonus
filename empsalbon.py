import sys
if len(sys.argv)==2:
    salary=int(sys.argv[1])

else:
    salary=50000

    bonus=salary+salary*(10/100)


    print("Total salary after adding bonus:",bonus)
