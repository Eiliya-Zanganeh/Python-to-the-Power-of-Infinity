def test_args(*args):
    print(args)

def test_kwargs(**kwargs):
    print(kwargs)


test_args('Eiliya', 'test')
# test_args(['Eiliya', 'test'])
test_args(*['Eiliya', 'test'])

test_kwargs(name='Eiliya', alaki='test')
# test_kwargs({'name':'Eiliya', 'alaki': 'test'}) # Have error
test_kwargs(**{'name':'Eiliya', 'alaki': 'test'})