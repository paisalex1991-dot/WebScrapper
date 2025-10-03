import sys

    
def main():
    with open('foo.txt', 'rt', encoding='utf-8') as f:
        for line in f:
    # here line is a *unicode* string

            with open('write_test', encoding='utf-8', mode='wt') as f:
                f.write('\u20ACunicode\u20AC\n') #  €unicoe€

if __name__ == '__main__':
    main()

