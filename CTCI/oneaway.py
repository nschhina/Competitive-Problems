def oneAway(str1, str2):
  lendiff = abs(len(str1) - len(str2))
  if lendiff > 1:
    return False
  elif lendiff == 0:
    difference = 0
    for i in xrange(len(str1)):
      if str1[i] != str2[i]:
        difference += 1
        if difference > 1:
          return False
    return True
  else:
    if len(str1) > len(str2):
      longer, shorter = str1, str2
    else:
      longer, shorter = str2, str1
    away = 0
    for i in xrange(len(shorter)):
      if shorter[i] != longer[i + shift]:
        if away or (shorter[i] != longer[i + 1]):
          return False
        away = 1
    return True
