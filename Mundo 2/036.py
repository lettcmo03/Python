loan=float(input('How much do you want to get as a loan? '))
worth=float(input('How nuch do you make in a month? '))
time=int(input('How long will it take for you to pay us off (in years)? '))
monthly=loan/(time*12)

if monthly > (30 / 100) * worth:
    print('Your loan has been DENIED')
else:
    print('Your loan has been APPROVED')
