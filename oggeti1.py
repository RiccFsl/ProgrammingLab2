class CSVFile():
    
    def __init__(self, name):
        self.name = name
        
    def get_data (self):
        lista = []
        try:
            my_file = open(self.name, 'r') 
        except Exception as e:
            print('Errore! il file "{}" non esiste'.format(self.name))
        for line in my_file:
            element = line.strip().split(',')
            #se non sto processando l'intestazione
            if element [0] != 'Date':
                lista.append(element)
        return lista