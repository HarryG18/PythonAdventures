def extract_primes(num):
    # get list of primes between 2 and num
    primes = set( range( 2, num + 1 ) )


    for i in range( 2, int( num ** 0.5 + 1 ) ):
        primes -= set( range( i * 2, num + 1, i ) )
    # get list of numbers to check if prime
    num_str = str( num )
    print( str( primes ) )
    chk_nums = [int( num_str[j:j + i + 1] ) for i in range( len( num_str ) ) for j in range( len( num_str ) - i ) if num_str[j] != "0"]
    return sorted( [n for n in chk_nums if n in primes] )

print(extract_primes(73))