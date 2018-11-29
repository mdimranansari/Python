# if statement example ===============================================================================================

if True:
    print('Yes, it is true')
if False:                       # This won't execute
    print('Yes, it is false')


# While statement Ex =====================================================================

number = 23
running = True
while running: # As long as running is True, keep running
    guess = int(input('Enter an integer : '))
    if guess == number:
        print('Congratulations, you guessed it.')
        # this causes the while loop to stop
        running = False
    elif guess < number:
        print('No, it is a little higher than that.')
    else:
        print('No, it is a little lower than that.')
else:
    print('The while loop is over.')
# Do anything else you want to do here
print('Done')


# ===============================================================================================

i=0
while i<10:
    print(i, end=' ')
    i+=1
    #++i #i++ doesn't work
print("\n"*2)

# The for..in loop ==============================================================================================

for i in range(1, 5):
    print(i)    # 1 is included 5 is excluded
else:
    print('The for loop is over')

print("\n"*2)


# If we supply a third number to range , then that becomes the step count =========================================

for i in range(1,7,2):
    print(i)    # 1 is included 5 is excluded
else:
    print('The for loop is over')

for i in range(1,8,2):
    print(i)    # 1 is included 5 is excluded
else:
    print('The for loop is over')


# ==========================================================

for i in list(range(5)):
    print("\t"*i,i)    # 0 is included 5 is excluded and print 5 numbers


# The break Statement ==========================================================

while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
print('Length of the string is', len(s))
print('Done')


# The break Statement ==========================================================

while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
        print('Length of the string is', len(s))
print('Done')
print('\t'*2)

while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    print('Length of the string is', len(s))
print('Done')
print('\t'*2)

while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
print('Length of the string is', len(s))
print('Done')
print('\t'*2)


# The continue Statement ============================================

# The continue statement is used to tell Python to skip the rest of the statements in the
#current loop block and to continue to the next iteration of the loop.

while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    if len(s) < 3:
        print('Too small')
        continue
    print('Input is of sufficient length')
# Do other kinds of processing here...


