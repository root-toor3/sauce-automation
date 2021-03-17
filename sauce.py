print('type your code :')
import webbrowser

code = input()
loop = 'sauce'
strURL = "nhentai.net/g/" + code
def page() :
    webbrowser.open_new_tab(strURL) ;
    
while loop == 'sauce' :
    print('type your code :')
    code = input()
page()

