def sum_csv(file_name):
    values = []
    file = open(file_name,'r')
    for line in file:
        element = line.split(',')
        if element[0] != 'Date':
            value = element[1]
            values.append(float(value))
    file.close()
    if(len(values)==0):
        return None
    else:
        return sum(values)