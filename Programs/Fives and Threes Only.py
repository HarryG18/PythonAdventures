def only_5_and_3(num):
    if num < 3:
        return False
    else:
        if num == 3 or num == 5:
            return True
        elif num%3==0 and num/3 < 5:
            return only_5_and_3(num/3) or only_5_and_3(num-5)
        else: 
            return only_5_and_3(num-5)


def only_5_and_3_2(n):
	if n == 3 or n == 5:
		return True
	if n < 3:
		return False
	return only_5_and_3(n - 5) or only_5_and_3(n / 3)


print(only_5_and_3(9))
