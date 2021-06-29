# what the build in reduce generally looks like
def _reduce(fn, sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = fn(result, x)
    return result
    
# find the max
l = [5, 8, 6, 10, 9]
reduce(lambda a, b: a if a > b else b, l)

# another version of any()
l = [0, '', None, 100]
reduce(lambda a, b: bool(a) or bool(b), l)



