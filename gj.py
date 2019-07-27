import sys, string, math
def reduceN( vg, mm) :
	if mm <= 0 : return vg

	if vg == 0 : return 10	# Fail
	p1 = reduceN(vg//10, mm)*10 + vg%10
	p2 = reduceN(vg//10, mm-1)
	if p1 < p2 :
		return p1
	else :
		return p2

vg,mm = input().split()
vg,mm = int(vg),int(mm)
print(reduceN(vg,mm))
