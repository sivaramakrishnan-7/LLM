
def get_stats(ids, counts = None):
    """
    takes the ids and counts its pairs. 

    Args:
        ids (list): list of token ids 
        counts (dict, optional):  Defaults to None, else we can give the existing counts.
        
    """
    counts = {} if counts is None else counts
    for pair in zip(ids, ids[1:]):
        counts[pair] = counts.get(pair,0)+1
    return counts

def merge(ids, pair, idx):
    """
    Args:
        ids (list): list of all token ids.
        pair (tuple): pairs of ids.
        idx (int): number with which frequent ids are replaced.
    """
    newids = []
    i = 0
    while i < len(ids):
        if i < len(ids) - 1 and ids[i] == pair[0] and ids[i+1] == pair[1]:
            newids.append(idx)
            i += 2
        else:
            newids.append(ids[i])
            i += 1
    return newids
    
class Tokenizer:
    def __init__(self):
        self.merges = {}
        self.pattern = ""
        self.special_tokens = {}

        
    def train(self,text,vocab_size,verbose=False):
        assert vocab_size >= 256
        num_merges = vocab_size - 256
        
        text_bytes = text.encode("utf-8")
        ids = list(text_bytes)
        self.vocab = {idx:bytes([idx]) for idx in range(256)}
        for i in range(num_merges):
            stats = get_stats(ids)
            pair = max(stats,key=stats.get)
            idx = 256 + i
            ids = merge(ids, pair, idx)
            
            self.merges[pair] = idx
            self.vocab[idx] = self.vocab[pair[0]] + self.vocab[pair[1]]
        if verbose:
            print(f"merge {i+1}/{num_merges}: {pair} -> {idx} ({self.vocab[idx]}) had {stats[pair]} occurances")
            
    def encode(self, text):
        pass
        
            
            
            
            
            
     
     
        
        
        
    

        
        
        
        