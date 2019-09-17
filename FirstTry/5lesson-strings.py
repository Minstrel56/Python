mystring = "bla bla"
name = "vASya puPKin"

print(name)
print(name.title()) # Делает заглавные первые буквы
print(name.upper()) # Все буквы заглавные; lower() - все маленькие буквы

print("Privet stroka nomer1\nPrivet stroka nomer2\n\n stroka nomer3")
print("Messages:\n\tMessage1\n\tMessage2\n\tMessage3\nEnd") # перенос строки и табуляция
print("Lower name: "+ name.lower())
print(name.upper() + name.lower() + name.title())

a = "  .  , 123  , .  dadya vasya  ... , .    ,     "
print(a)
print(a.rstrip()) # стирает пробел справа
print(a.lstrip().rstrip()) #  стирает пробле слева и справа
print(a.strip()) #  стирает пробле слева и справа (как lstrip().rstrip() )
print("============")
print(a.strip(" "+","+".")) # убирает смволы пробела точки изапятой (До первого неисключенного символа слева и справа)