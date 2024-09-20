touch myfile.txt # create a file
echo "Hello World" > myfile.txt # write to file
curl www.google.com -o google.txt # -o option to save the output to a file
LC_ALL=C sed -i '' -e 's/google/firefox/' google.txt # set LC_ALL=C in order to avoid sed: RE error: illegal byte sequence
grep -lir firefox # search for a string in files