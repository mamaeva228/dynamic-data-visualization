from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2.QtWidgets import QListView
from PySide2.QtGui import QStandardItemModel, QStandardItem
from PySide2.QtGui import QImageReader, QIcon


# <div>Icons made by <a href="https://www.flaticon.com/authors/dave-gandy" title="Dave Gandy">Dave Gandy</a> from <a href="https://www.flaticon.com/" 			    title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" 			    title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>
# <div>Icons made by <a href="https://www.flaticon.com/authors/gregor-cresnar" title="Gregor Cresnar">Gregor Cresnar</a> from <a href="https://www.flaticon.com/" 			    title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" 			    title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>
# <div>Icons made by <a href="https://www.freepik.com/" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" 			    title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" 			    title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>




def supported_image_extensions():
    ''' Get the image file extensions that can be read. '''
    formats = QImageReader().supportedImageFormats()
    # Convert the QByteArrays to strings
    return [str(fmt) for fmt in formats]

if  __name__== "__main__":
    import sys
    app = QApplication(sys.argv)

    lst = QListView()    
    lst.setMinimumSize(600, 400)
    model = QStandardItemModel(lst)

    item = QStandardItem()
    item.setText('Item text')
    item.setIcon(QIcon('icons/table-grid.svg'))    
    item.setEditable(False)

    model.appendRow(item)


    
    lst.setModel(model)

    lst.show()
    
    sys.exit(app.exec_())




