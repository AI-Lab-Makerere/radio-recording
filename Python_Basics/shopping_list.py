# created by JM
# Ordering things from a meat shop
# GitHub for Education to create private repositories
# Use stuff on Jet Brains for free with your university email
# Use anaconda

print('What is your name?')
customer_name = input()  # commenting out code
customer_name='Jonathan'
print('It is good to meet you, ' + customer_name)
print('The length of your name is:')
print(len(customer_name))

order_complete= True
spam = 10
inbox = 20
age=28


if spam < 0:
    print(spam)
else:
    print (inbox)

if customer_name == 'Alice':
    print('Hi, Alice.')
elif age > 18:
    print('You are grown up now, ' +customer_name +'')
else:
    print ('Scholarship given')