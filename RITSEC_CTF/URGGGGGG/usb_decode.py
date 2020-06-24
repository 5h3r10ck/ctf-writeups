alpha ={
   0X04:"A", 0X05:"B", 0X06:"C", 0X07:"D", 0X08:"E", 0X09:"F",
   0X0A:"G", 0X0B:"H", 0X0C:"I", 0X0D:"J", 0X0E:"K", 0X0F:"L",
   0X10:"M", 0X11:"N", 0X12:"O", 0X13:"P", 0X14:"Q", 0X15:"R",
   0X16:"S", 0X17:"T", 0X18:"U", 0X19:"V", 0X1A:"W", 0X1B:"X",
   0X1C:"Y", 0X1D:"Z", 0X1E:"1!", 0X1F:"2@", 0X20:"3#", 0X21:"4$",
   0X22:"5%", 0X23:"6^", 0X24:"7&", 0X25:"8*", 0X26:"9(", 0X27:"0)",
   0X2C:"  ", 0X2D:"-_", 0X2E:"=+", 0X2F:"{", 0X30:"}",  0X32:"#~",
   0X33:";:", 0X34:"'\"",  0X36:",<",  0X37:".>",0X4f:">", 0X50:"<",
   0X39:"[CAPS]", 0X2A:"[DEL]",0x59:"1", 0X1E:"!", 0X1F:"2@", 0X20:"3#",0X21:"$4",
   0X22:"5%", 0X23:"^6", 0X24:"7&", 0X25:"*8",0X26:"9(", 0X27:"0)", 0X28:"[ENTER]",
   0X38:"/?", 0X55:"*", 0X56:"-", 0X57:"+",0X58:"[ENTER]",0X59:"1",
   0X5A:"2",0X5B:"3",0X5C:"4",0X5D:"5", 0X5E:"6", 0X5F:"7", 0X60:"8",0X29:"[ESC]",
   0X61:"9",0X62:"0", 0X4E:"UP", 0X4F:"[DOWN]", 0X50:"[LEFT]",0X51:"[DOWN]",0X52:"[RIGHT]"
   }

nums = []

keys = open('usbdata.txt')

for line in keys:
    nums.append(int(line[6:8],16))

keys.close()
output = ""
for n in nums:
    if n == 0 :
        continue
    if n in alpha:
          output += alpha[n]
    else:
        output += '[...]'
print(output)

