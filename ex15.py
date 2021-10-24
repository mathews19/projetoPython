from sys import argv

script = argv # file_name = argv Nessa linha recebemos/descompactamos os parametros recebidos
file_name = input("Digitev aqui o nome do arquivo")
txt = open(file_name) # Nessa linha abrimos o arquivo que recebemos como parametro no command line

print(f"Here\'s your file {file_name}: ")
print(txt.read()) # Nessa linha abrimos e lemos o arquivo
txt.close()

print("Type the file name again: ") # Aqui colocamos o nome novamente do arquivo que queremos ler
file_again = input("> ")

txt_again = open(file_again) # Aqui o arquivo será aberto novamente 

print(txt_again.read()) # E aqui executamos a leitura do arquivo
txt_again.close()

