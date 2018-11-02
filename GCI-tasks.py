# This part is the loop one
run = True
i = 0
while run:
    if i == 10 :
       run = False
    else :
        print("GCI is great")
        i +=1
# This part is for user's name
a = input ("What is your name ?")
print ("Hello " + a + ", please to meet you!")
print ("Did you know that your name backwards is", a[::-1])
