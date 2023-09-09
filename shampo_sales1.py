def sum_csv(file_name):
    values = []
    for line in file_name:
        element = line.split(',')
        if (element[0] != 'Date'):
            value = element[1]
            values.append(value)
    return sum(values)
    
my_file = open('shampoo_sales.csv', 'r')
sum_csv(my_file)