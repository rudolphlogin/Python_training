def greet(lang):
  if lang == "es":
    return "Namaste"
  elif lang == "fr":
    return "good morning"
  else:
    return "hello"

print (greet('es'))
print (greet('fr'))

x = greet('es')
print(x)
