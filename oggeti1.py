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

class NumericalCSVFile(CSVFile):
    
    def get_data(self):
        original_data = super().get_data()  # Ottieni i dati originali dalla classe padre
        converted_data = []

        for row in original_data:
            converted_row = [row[0]]  # Mantieni il primo elemento come stringa
            for item in row[1:]:
                try:
                    # Converte gli elementi in float, escludendo il primo elemento
                    converted_row.append(float(item))
                except ValueError:
                    # Se la conversione in float fallisce, mantieni il valore come stringa
                    print('Errore! "{}" non può essere convertito a float')
                    converted_row.append(item)
            converted_data.append(converted_row)

        return converted_data