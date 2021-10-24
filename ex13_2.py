from sys import argv
script, first, second = argv

print "Originais: ", argv[0], argv[1], argv[2]
argv[0] = raw_input("argumento 0? ")
argv[1] = raw_input("argumento 1? ")
argv[2] = raw_input("argumento 2? ")

print "Novos: ", argv[0], argv[1], argv[2]

