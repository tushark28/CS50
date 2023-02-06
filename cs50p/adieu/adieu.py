List = []
while True:
    try:
        List.append(input("Name: "))

    except EOFError:
        new="Adieu, adieu, to "
        for i in range(len(List)-1):
            new += f"{List[i]}, "
        if len(List) == 1:
            new += f"{List[0]}"
        elif len(List) == 2:
            new.replace(',','',3)
            new+= f"and {List[len(List)-1]}"
        else:
            new+= f"and {List[len(List)-1]}"
        print(new)
        break