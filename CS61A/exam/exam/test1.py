def longest_increasing_suffix(n):
	m,suffix,k=10,0,1
	while n:
		n,last = n//10,n%10
		if last<m:
			m,suffix,k=last,suffix+k*last,k*10
		else:
			return suffix
	return suffix

def sandwich(n):
	tens,ones=n%10,n%100//10
	n=n//100
	while n:
		if n%10 == tens:
			return True
		else:
			tens,ones=ones,n%10
			n=n//10
	return False

def luhn_sum(n):
	def luhn_number(digital):
		x=digital * multiplier
		return x//10+x%10
	total,multiplier=0,1
	while n:
		n,last=n//10,n%10
		total += luhn_number(last)
		multiplier = 3 - multiplier
	return total
