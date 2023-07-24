a=input()
b=input()
c=input()
d=int(b)**2-4*int(a)*int(c)
d1=d**0.5
if d<0:
    print("Imaginary parts")
else:
    root1=(-int(b)-d1)/2*int(a)
    root2=(-int(b)+d1)/2*int(a)
    print(root1)
    print(root2)
