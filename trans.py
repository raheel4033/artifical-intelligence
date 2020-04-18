import hashlib as h
import pickle as pk

block = {
    'transactions':[{
        'from' : 'A',
        'to' : 'B',
        'amount' :10

    },
        {
            'from':'B',
            'to':'C',
            'amount':10
        },
        {
            'from':'C',
            'to':'D',
            'amount':10,
            'message':'Thanks for the help'
        },
    ]
}
n = h.sha3_256()
n.update(pk.dumps(block))
n.digest()
n.hexdigest()

