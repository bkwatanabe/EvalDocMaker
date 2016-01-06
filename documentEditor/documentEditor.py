import gtk#, webkit
import webbrowser

win = gtk.Window()
win.show()
win.connect('destroy', lambda w: gtk.main_quit())
win.resize(300,300)



# web = webkit.WebView()
# web.open('file:///Users/brettwatanabe/PycharmProjects/EvalDocMaker/documentEditor/initial-evaluation.html')
scroller = gtk.ScrolledWindow()
#scroller.add(web)

win.add(scroller)
