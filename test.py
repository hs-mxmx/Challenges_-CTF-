

password_usuario_input = [55,56,54,79,115,69,114,116,107,49,50];

password_programa = [70,65,85,88,32,80,65,83,83,87,79,82,68,32,72,65,72,65];

#tab2 = [55,56,54,79,115,69,114,116,107,49,50];

tab2 = password_programa
tab = password_usuario_input

#i = 0
#j = 0
#k = 0
l = 0
#
#m = "";
#n = "";
#o = "";
p = "";

i = 0;
j = len(tab)

n = 0

k = j + l + n
n = len(tab2)
a = "";

#for(i = (o=0); i < (k = j = n); i++ ){
# o = tab[i-l];
# p += String.fromCharCode((o = tab2[i]));
# if(i == 5)break;}
for x in range(0,n):
  o = tab[x-l]
  p +=  chr(tab2[x])
  if ( x == 5):
    break

#for(i = (o=0); i < (k = j = n); i++ ){
#  o = tab[i-l];
# if(i > 5 && i < k-1)
# p += String.fromCharCode((o = tab2[i]));
for x in range(0,len(tab)):
  o = tab[x-l]
  if (x > 5 and i < n-1):
    p += chr(tab2[x])

   # String["fromCharCode"](dechiffre("\x35\x35\x2c\x35\x36\x2c\x35\x34\x2c\x37\x39\x2c\x31\x31\x35\x2c\x36\x39\x2c\x31\x31\x34\x2c\x31\x31\x36\x2c\x31\x30\x37\x2c\x34\x39\x2c\x35\x30"));

for z in range(0,len(tab)):
  o = tab[x-l]
  a += chr((tab[z]))

p += chr(tab2[17])
print(a)
print(p)


