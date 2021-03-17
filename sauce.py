import webbrowser
def mainfunction() :
    print('Type your code :')
    code = input()
    strURL = "nhentai.net/g/" + code
    webbrowser.open_new_tab(strURL) ;  
loop = 'sauce'
while loop == 'sauce' :
    mainfunction()
