a = 1
b = 5
a += 1
a *= 2

print("le type de a est ", type(a))
print("le type de b est ", type(b))

a /= 2
a,b = b,a

texte = "super"
print("Python est " + texte)

print("le type de a est ", type(a))
print("le type de b est ", type(b))
print("le type de texte est ", type(texte))

print("a=", a, "et b=", b)
b = int(b)

c = a == b
print("c=", c)

d = a // b
e = a % b
print("d=", d, "et e=", e)
