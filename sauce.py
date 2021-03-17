print('type your code :')
import webbrowser
code = input()
strURL = "nhentai.net/g/" + code
def page() :
    webbrowser.open_new_tab(strURL) ;  
page()

