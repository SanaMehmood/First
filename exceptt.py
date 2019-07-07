a = {'Name':'Sana'}
try:
    with open('data.csv', 'w'):
        print('Iam after open')
    print(a['Name'])

except KeyError:
    print('This key doesnt exist')
except FileNotFoundError as e:
    print(e)
    print('File doesnt exist')

except Exception:
    print('Unknown error')
finally:
    print('Iam finally block')
print('Ending')
