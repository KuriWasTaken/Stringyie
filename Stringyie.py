def AdvancedStringError(Str):
  print("\033[31m"+"Stringyie Error: "+Str+"\033[0m")
  exit(1)

def SplitFromTo(Str, From, To, Include):
  newString = ""
  Started = False
  for i in Str:
    if Started == True:
      if not i == To:
        newString += i
      else:
        if Include:
          newString += i
        return newString
    if i == From:
      if Include:
        newString += i
      Started = True
  if Started == False:
    AdvancedStringError("Could not find the start of split in: "+Str)
  else:
    AdvancedStringError("Could not find the end of split in: "+Str)
def CountSize(Str):
  count = 0
  for i in Str:
    count+=1
  return count
def RemoveAllOfCharInStr(Str, Char):
  newString = ""
  for i in Str:
    if i != Char:
      newString += i
  return newString
def RemoveFirstOfCharInStr(Str, Char):
  newString = ""
  Found = False
  for i in Str:
    if i == Char and Found == False:
      Found = True
    else:
      newString += i
  return newString
def RemoveFinalOfCharInStr(Str, Char):
  newString = ""
  Found = False
  for i in Str[::-1]:
    if i == Char and Found == False:
      Found = True
    else:
      newString += i
  return newString[::-1]
def GetCharAtIndex(Str, Idx):
  count = 1
  for i in Str:
    if count == Idx:
      return i
    count += 1
  AdvancedStringError("Índex is out of range at: "+Str)
def SetCharAtIndex(Str, Idx, To):
  newString = ""
  count = 1
  for i in Str:
    if not count == Idx:
      newString += i
    else:
      newString += To
    count += 1
  if len(Str) < Idx:
    AdvancedStringError("Índex is out of range at: "+Str)
  return newString
def SplitStrToArrayByChar(Str):
  Arr = []
  for i in Str:
    Arr.append(i)
  return Arr
def SplitStrByChar(Str, Char, Include):
  Arr = []
  currentStr = ""
  for i in Str:
    if i == Char:
      if Include:
        currentStr += i
      Arr.append(currentStr)
      currentStr = ""
    else:
      currentStr += i
  Arr.append(currentStr)
  return Arr
def ReplaceAllOccurrencesOfChar(Str, From, To):
  newString = ""
  for i in Str:
    if i == From:
      newString += To
    else:
      newString += i
  return newString
def ReplaceFirstOccurrencesOfChar(Str, From, To):
  newString = ""
  Found = False
  for i in Str:
    if i == From and Found == False:
      Found = True
      newString += To
    else:
      newString += i
  return newString
def ReplaceFinalOccurrencesOfChar(Str, From, To):
  newString = ""
  Found = False
  for i in Str[::-1]:
    if i == Char and Found == False:
      Found = True
      newString += To
    else:
      newString += i
  return newString[::-1]
def EncodeStrToNumbers(Str):
  Chars = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWZXY0123456789 !"#¤%&/()=?`@£$€{[]}\^~¨'*-_,.<>|§½"""
  Count = 1
  newStr = ""
  for i in Str:
    for a in Chars:
      if i == a:
        newStr += "0" + str(Count)
        Count = 1
        break
      Count += 1
  return newStr
def DecodeStrToNumbers(Str):
  if not Str.isnumeric():
    AdvancedStringError("Can only decode numbers at: "+Str)
  Chars = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWZXY0123456789 !"#¤%&/()=?`@£$€{[]}\^~¨'*-_,.<>|§½"""
  newStr = ""
  for i in SplitStrByChar(Str, "0", False):
    if i.isnumeric():
      newStr += Chars[int(i)-1]
  return newStr  
