def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
print_params(a = 1, b = 'строка', c = True)
print_params('AA', True)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [1, 'строка', True]
print_params(*values_list)
values_dict = {1,'строка', True}
print_params(*values_dict)

values_list_2 = [5,'лист']
print_params(*values_list_2, 42)
