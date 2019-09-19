
def camel_case(txt):
  txt_arr = txt.split(' ')
  for idx, t in enumerate(txt_arr):
    txt_arr[idx] = t.capitalize()
  return ''.join(txt_arr)
