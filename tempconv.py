#tempconv.py

'''This program will convert temperatures between
F and C'''

def conv(temp, t_type):
  if t_type == 'c' or t_type == 'C':
    cel = (temp - 32) * 5/9
    return cel
  else:
    fahr = temp*9/5 + 32
    return fahr

def main():
  print 'Temperature Converter'
  temp = float(raw_input("Temperature: "))
  t_type = raw_input("Convert to (F)ahrenheit or (C)elsius? ")
  print conv(temp, t_type)
  
main()
