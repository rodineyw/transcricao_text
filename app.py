import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog
from PyQt5.QtGui import QIcon
import pytesseract
from PIL import Image
import fitz


class MainWindow(QMainWindow):
    def __init__(self):
        """
        Constructor for the class, initializes the UI.
        """
        super().__init__()

        self.initUI()

    def initUI(self):
        """
        Initializes the UI by setting the geometry, window title, central widget, and creating actions and menus.
        """
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Extrator de Texto")

        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        self.createActions()
        self.createMenus()

        # implementação do método extractText

    def extractText(self):
        """
        A method that extracts text. Calls extractTextFromPDF and extractTextFromImage.
        """
        self.extractTextFromPDF()
        self.extractTextFromImage()
        self.saveTextToFile()

    def createActions(self):
        """
        Creates and initializes the actions for opening a file and extracting text.
        """
        self.openFileAction = QAction(QIcon("open.png"), "Abrir", self)
        self.openFileAction.setShortcut("Ctrl+O")
        self.openFileAction.triggered.connect(self.openFile)

        self.extractTextAction = QAction("Extrair Texto", self)
        self.extractTextAction.setShortcut("Ctrl+E")
        self.extractTextAction.triggered.connect(self.extractText)

    def createMenus(self):
        """
        Create menus in the menu bar.
        """
        menubar = self.menuBar()
        fileMenu = menubar.addMenu("Arquivo")

        fileMenu.addAction(self.openFileAction)

        extractMenu = menubar.addMenu("Extrair")
        extractMenu.addAction(self.extractTextAction)

    def openFile(self):
        """
        Opens a file dialog to allow the user to select a file.
        Clears the text edit widget and sets the plain text content based on the selected file type.
        """
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(
            self,
            "Abrir arquivo",
            "",
            "PDF (*.pdf);;Imagem (*.jpg *.png *.jpeg)",
            options=options,
        )

        if fileName:
            self.text_edit.clear()
            if fileName.lower().endswith((".jpg", ".png")):
                text = self.extract_text_from_image(fileName)
            elif fileName.lower().endswith(".pdf"):
                text = self.extract_text_from_pdf(fileName)
            else:
                text = "Formato de arquivo não suportado"

            self.text_edit.setPlainText(text)

    def extract_text_from_image(self, image_path):
        """
        Extracts text from an image using Tesseract OCR.

        Args:
            image_path (str): The path to the image file.

        Returns:
            str: The extracted text from the image.
        """
        text = pytesseract.image_to_string(Image.open(image_path))
        return text

    def extract_text_from_pdf(self, pdf_path):
        """
        Extracts text from a PDF file.

        Args:
            pdf_path (str): The path to the PDF file.

        Returns:
            str: The extracted text from the PDF.
        """
        text = ""
        doc = fitz.open(pdf_path)
        for page in doc:
            text += page.get_text()
        return text

    def saveTextToFile(self):
        text = self.text_edit.toPlainText()
        if text:
            options = QFileDialog.Options()
            fileName, _ = QFileDialog.getSaveFileName(
                self,
                "Salvar como",
                "",
                "Arquivo de Texto (*.txt)",
                options=options,
            )
            if fileName:
                with open(fileName, "w") as f:
                    f.write(text)
                    f.close()


def main():
    """
    A function to initialize the application, create and show the main window, and start the application event loop.
    """
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
