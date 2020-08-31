def media():
    pri = int(input('Digite a primeira nota:'))
    seg = int(input('Digite a segunda nota:'))
    ter = int(input('Digite a terceira nota:'))
    med = (pri + seg + ter) / 3
    if med > 8:
        med + 1
    if med >= 10:
        med = 10
    print("%.2f" %med)
def main():
    media()
if __name__=='__main__':
    main()


