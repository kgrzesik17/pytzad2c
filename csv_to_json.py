def csv_to_json(name:str, new:str, tuple_separator=';', line_separator="\n"):
    '''
    This function reads the CSV file and converts it to JSON

    Arguments:
    name - name of a CSV file you want to convert.
    new - name of a new JSON file you want to create.
    tuple_separator - character used in the CSV file to mark a tuple separator.
    row_separator - character used in the CSV file to mark a row separator.
    '''

    temp = ""
    temp_array = []

    values = []

    try:
        file = open(name, "r")
    except FileNotFoundError:
        print("Nie znaleziono pliku.")
        return False
    
    for line in file:
        for char in line:
            if char != tuple_separator and char != line_separator:
                temp += char
            else:
                temp_array.append(temp)
                temp = ""
        is_first = False
                
        values.append(temp_array) # TBD: last tuple isn't added if there is no line separator at the end
        temp_array = []

    keys = values[0]
    values.pop(0)

    print(keys)
    print(values)
                

csv_to_json('plik.csv', 'test.json')