
if __name__ == "__main__":
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for var, exp in cs_utils.dict_statement_reader(sys.stdin):
        exec(var + " = " + exp)

    
    result = # Call Challenge Function Here
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
