import csv
with open("C:/Users/CarlosViniMSouza/Documents/Programacao/Programacao_R/R_Code/Aprofundando-R/Pesquisa-Pessoal/Iris.csv") as file:
    archive = csv.reader(file)
    for all in archive:
        print(all)