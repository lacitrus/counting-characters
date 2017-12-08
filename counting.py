dic = {}

#sentence = input("Please enter a sentence:")
sentence ="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc accumsan sem ut ligula scelerisque sollicitudin. Ut at sagittis augue. Praesent quis rhoncus justo. Aliquam erat volutpat. Donec sit amet suscipit metus, non lobortis massa. Vestibulum augue ex, dapibus ac suscipit vel, volutpat eget massa. Donec nec velit non ligula efficitur luctus."

for char in sentence:
    if char in dic:
        dic[char] =  dic[char] + 1
    else:
        dic[char] = 1
        
              
              
for a in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,.':
    if a in sentence:
        print(a, dic[a]) 