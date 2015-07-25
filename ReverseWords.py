import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test != '\n':
        test = test.strip()
        sentence_list = test.split(' ')
        sentence_list = sentence_list[::-1]
        print ' '.join(sentence_list)







