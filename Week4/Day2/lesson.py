email = input ('enter your gmail address')
gmail = @gmail.com
name = joshua
name + gmail = joshua@gmail.com

#option one - slice
email = 'bob@gmail.com'
email[-1:-10]       #@gmail.com [starts at m, ends at @]

#option 2 - split
text = "bob@gmail.com"
print (text.split('@')[0])

result = email.split('@')

