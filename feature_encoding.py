
def is_true(x):
  if x:
    return 1
  else:
    return 0
  
def greater_than_zero(x):
  ''' If the value is greater than zero return 1 otherwise return 0'''
  if x > 0:
    return 1
  else:
    return 0

def encode_gender(x):
  if x in ['M', 'F']:
    return x
  else:
    return 'other'

def encode_browser(x):
  if x in ['Chrome', 'Facebook', 'Safair', 'Webview/iOS']:
    return x
  else:
    return 'other'
  
