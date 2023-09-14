class CSVFile():
    
    def __init__(self, name):
        self.name = name
        self.lista = []  # Inizializza la lista vuota
        
        try:
            with open(self.name, 'r') as my_file:
                for line in my_file:
                    element = line.strip().split(',')
                    # Se non sto processando l'intestazione
                    if element[0] != 'Date':
                        self.lista.append(element)

        except Exception as e:
            print('Errore! il file "{}" non esiste'.format(self.name))

    def get_data(self):
        return self.lista
