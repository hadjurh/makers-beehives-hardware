from subprocess import call

call(['mogrify', '-resize', '800x600', '*.jpg'])
print('>>>> images resized')
