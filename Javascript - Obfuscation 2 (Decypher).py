import math
#var ð= #"\x71\x11\x24\x59\x8d\x6d\x71\x11\x35\x16\x8c\x6d\x71\x0d\x39\x47\x1f\x36#\xf1\x2f\x39\x36\x8e\x3c\x4b\x39\x35\x12\x87\x7c\xa3\x10\x74\x58\x16\xc7\#x71\x56\x68\x51\x2c\x8c\x73\x45\x32\x5b\x8c\x2a
#\xf1\x2f\x3f\x57\x6e\x04\x3d\x16\x75\x67\x16\x4f\x6d\x1c\x6e\x40\x01\x36\#x93\x59\x33\x56\x04\x3e\x7b\x3a\x70\x50\x16\x04\x3d\x18\x73\x37\xac\x24\x#e1\x56\x62\x5b\x8c\x2a\xf1\x45\x7f\x86\x07\x3e
#\x63\x47";



def funcion1(x,y):
  return x^y;


def funcion2(y):
  z = 0
  for i in range(0,y):
    z += math.pow(2,i)
  return z


def funcion3(y):
  z = 0
  i = 8-y
  for i in range (i<8):
    z += math.pow(2,i)
  return z


def funcion4(x,y):
  y = y % 8
  l = funcion2(y)
  l = (x and l) << (8-y)
  return (l + (x>>y))


def funcion5(x,y):
  y = y % 8
  l = funcion3(y)
  l = (x and l) >> (8-y)
  return ((l+(x<<y))and 0x00ff)


def funcion6(x,y):
  return funcion5(x,y)

def funcion7(funcion9,key):
  funcion8 = ""
  funcion8_2 = ""
  for i in range (i<len(funcion9)):
    c = chr(funcion9[i])
    if(i != 0):
      t = funcion8([i-1])%2
      if t == 0:
        cr = funcion1(c,chr(key[i % len(key)]))
      elif t == 1:
        cr = funcion6(c,chr(key[i % len(key)]))
    else:
      cr =  funcion1(c,chr(key[i % len(key)]))
    funcion8 += chr(cr)
  return funcion8


def funcion10(p):
  n = 0
  for i in range(i<len(p)):
    n += chr(p[i])
  if(n == 8932):
    ç = window.open("","","\x77\x69\x64\x74\x68\x3d\x33\x30\x30\x2c\x68\x65\x69\x67\x68\x74\x3d\x32\x20\x30")
    ç.document.write(p)
  else:
    print("Mauvais mot de passe!")

funcion10(funcion7(o,print("Mot de passe?")))
      
