class Fasta:
    def __init__(self,file):
        self.file = file
    
    def file(self):
        return self._file

    # instance DNA seq
    def instance_DNA(self,Sequence_class):
        with open(self.file) as file:
            for line in file:
                line=line.rstrip()
                if line.startswith('>'):
                    id = line.lstrip('>')
                    seq = next(file).rstrip()
                
                yield Sequence_class(id,seq)

#seq4= DNA_Sequence('gene', 'ACTGTTTT')
#print(f'{seq4}')
#print(f'len({seq4})')
#print (f'{seq4.translate_seq()}')

        