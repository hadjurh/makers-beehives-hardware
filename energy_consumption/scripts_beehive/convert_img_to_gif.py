from subprocess import call

call(['convert', '-delay', '25', '-loop', '0', '*.jpg', 'capture.gif'])
print('>>>> gif created')
