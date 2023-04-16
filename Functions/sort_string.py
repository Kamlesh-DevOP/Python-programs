def sort_string(str1):
    x=str1.split('-')
    x.sort()
    return '-'.join(x)

print(sort_string('green-red-yellow-black'))