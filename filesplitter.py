
def write_new(line):
    chunks = line.split(';')
    fname = './out/rep'+chunks[0].strip()+'.txt' 
    with open(fname, 'a') as nf:
        nf.write(line)
       
if __name__ == '__main__':
    inputfile = 'clientes_bloq.txt'
    with open(inputfile,'r') as file:
        for l in file:
            write_new(l)        
            