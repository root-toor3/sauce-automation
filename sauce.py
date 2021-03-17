print('type your code :')
import webbrowser

code = input()
loop = 'hello'
strURL = "nhentai.net/g/" + code
def page() :
    webbrowser.open_new_tab(strURL) ;
    
while loop == 'hello' :
    print('type your code :')
    code = input()
page()

