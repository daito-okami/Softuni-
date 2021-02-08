from modules.fibonacci_sequence.fibonacci_sequence import create_sequance, locate


commands =[
    'Create Sequence 10',
    'Locate 13',
    'Create Sequence 3',
    'Locate 10',
    'Stop'
]


for command in commands:
    if 'Create' in command:
        pass
    else:
        pass


print(create_sequance(10))
print(locate(13))