class Sequence:
    # constructor
    def __init__(self, id, seq):
        self._id = id
        self._seq = seq.upper()
        
    # getter and setter for id
    @property
    def id(self):
        return self._id   
        # getter and setter for seq
    @property
    def seq(self):
        return self._seq
    
# create the class
    # method to return id and the seq
    def create_fasta(self):
        fasta=f'>{self.id}\n{self.seq}\n'
        return fasta
    
    def __str__(self):
        return f'sequence object: ID {self.id}, seq; {self.seq}'

    def __len__(self):
        return f'length of the sequence is {len(self.seq)}'


class DNA_Sequence(Sequence):
   


    
    # the setter is here as an example
    """
    @seq.setter
    def seq(self, seq):
        self._seq = seq.upper()
    """
    def __str__(self):
        return f'DNASequence object: ID {self.id}, seq; {self.seq}'
       
    # gc content method
    def calc_gc_content(self, dp=2):
        c_count = self.seq.count('C')
        g_count = self.seq.count('G')
        gc_content = (c_count + g_count) / len(self.seq)
        return round(gc_content, dp)
    
    # method to translate sequence
    def translate_seq(self):
        bases = "tcag".upper()
        codons = [a + b + c for a in bases for b in bases for c in bases]
        amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
        codon_table = dict(zip(codons, amino_acids))
        translated_seq = ''
        for i in range(0,len(self.seq)-2,3):
            triplet = self.seq[i:i+3]
            aa = codon_table[triplet]
            translated_seq += aa
        return translated_seq
    

    # get protein length 
    def get_protein_len(self):
        return len(self.seq) // 3
    # method to return id and the seq
    def create_fasta(self):
        fasta=f'>{self.id}\n{self.seq}\n'
        return fasta


# create the class
class Protein(Sequence):
    def __init__(self, id, seq, descr='unknown'):
        super().__init__(id, seq)
        self._descr = descr
        
    # getter and setter for seq
    @property
    def seq(self):
        return self._seq
    
    @property
    def descr(self):
        return self._descr
    # the setter is here as an example
    """
    @seq.setter
    def seq(self, seq):
        self._seq = seq.upper()
    """
    
    def __str__(self):
        return f'Protein object: ID {self.id}, seq; {self.seq}'
       
    # gc content method
    def calc_hydro_content(self, dp=2):
        a_count = self.seq.count('A')
        i_count = self.seq.count('I')
        l_count = self.seq.count('L')
        m_count = self.seq.count('M')
        f_count = self.seq.count('F')
        w_count = self.seq.count('W')
        y_count = self.seq.count('Y')
        v_count = self.seq.count('V')
        hydro_content = (a_count + i_count + l_count + m_count + f_count + w_count + y_count + v_count) / len(self.seq)
        return round(hydro_content, dp)
  
    # get protein length 
    def get_protein_len(self):
        return len(self.seq) 