#終極密碼遊戲
def ultimate_password():
    ans=np.random.randint(0,101)
    while True:
        try:
            pwd=int(input('請輸入0-100的數字'))
            pwd=int(pwd)
            if pwd>100 or pwd <0:
                print('超出範圍')
            if int(pwd)==int(ans):
                print('Bingo!')
                break
            elif int(pwd)>int(ans):
                print('密碼比%s小'%pwd)
            elif int(pwd)<int(ans):
                print('密碼比%s大'%pwd)
        except:
            print('請輸入數字')
