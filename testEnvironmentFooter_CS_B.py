    if isinstance(result, int) or isinstance(result, str):
        fptr.write(str(result))
    elif isinstance(result, list) or isinstance(result, tuple):
        fptr.write(str(result))
    else:
        fptr.write(' '.join(map(str, iter(result))))
        
    fptr.write('\n')

    fptr.close()