class CSVFile():
    
    def __init__(self, name):
        self.name = name
        self.lista = []  # Inizializza la lista vuota
        
        try:
            my_file = open(self.name, 'r')
            for line in my_file:
                element = line.strip().split(',')
                # Se non sto processando l'intestazione
                if element[0] != 'Date':
                    self.lista.append(element)
            my_file.close()  # Chiudi il file dopo aver terminato di leggerlo
        except Exception as e:
            print('Errore! il file "{}" non esiste'.format(self.name))

    def get_data(self):
        return self.lista
