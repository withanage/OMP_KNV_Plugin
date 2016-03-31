# Metadata-Export Tool

This tool exports metadata files for the print-on-demand (POD) service of KNV (Link)(Koch, Neff & Volckmar GmbH).The POD service demands for each monograph/edited volume four different files: 
* 1 PDF file containing the cover page
* 1 PDF file containing the content of the monograph
* 1 XML file containing metadata (ONIX-XML format) 
* 1 XML file containing metadata (local XML scheme defined by KNV)

In our use case, administration and maintenance of metadata is done in the Open Monograph Press (OMP)(Link). Since OMP is not able to export ONIX- and KNV-XML formats as defined by KNV, the Metadata-Export Tool reads metadata entered into OMP and converts it into the two XML formats required by KNV. The tool provides extra form-based input masks for metadata which can not be entered into OMP.

The Metadata-Export Tool is web-based and is able to export XML files.

## Requirements

Following requirements are necessary for the use of the Metadata-Export Tool:

* the Python programming language ([version 2.7](https://www.python.org/download/releases/2.7/)) 

* the Python web framework [web2py](http://www.web2py.com/init/default/download)

* the [MySQL](https://www.mysql.de/downloads/) database

## Technologies

Following technologies and software are used in the development of the Metadata-Export tool: XML, ONIX, web2py and Markdown.

### XML

[XML](https://en.wikipedia.org/wiki/XML) (Extensible Markup Language) is a text-based data format for exchanging hierarchically structured information. The main advantages of XML are easy-readability, simplicity of the syntax and easy adaptability with standardised processing models.

### ONIX

[ONIX](http://home.bic-media.com/index.php/onix-2-1) (Online Information Exchange) is an XML-based data format found by  [EDItEUR](http://www.editeur.org/83/Overview/), an  international organization coordinating development of the standards in e-commerce. ONIX data format is used to exchange bibliographic and product information among publishers, booksellers (e.g. [Amazon.com, Inc.](http://www.amazon.com/books-used-books-textbooks/b?ie=UTF8&node=283155)), libraries and other stakeholders in the book trade.

### web2py

The open source web framework [web2py](http://web2py.com/books/default/chapter/29/01/introduction), written in the Python programming language, is used for the development of database-based software. The Python framework web2py includes all the components which are needed to build fully functional web applications.

### Markdown

[Markdown](https://guides.github.com/features/mastering-markdown/) is a simplified and easily readable markup language. Texts written in the Markdown language can be automatically converted into other text formats such as PDF, HTML and MS-Word easily.

## User Manual

<img src="https://raw.githubusercontent.com/withanage/OMP_KNV_Plugin/master/static/images/readme/figure1.png">

Figure 1 shows the index page of the Metadata-Export Tool. By clicking on the 'Bücher' hyperlink in the navigation menu, you can see a table showing all monographs sorted by their descending 'submission_ID' and consisting of six columns: 1) submission ID, 2) setting value (title), 3) date submitted, 4) status, 5) KNV-XML and 6) ONIX. In the status column you can see if the metadata of a monograph has been already sent to KNV or if it has still to be done. In the last to columns you can find hyperlinks directly leading to the download of the KNV- and the ONIX-XML file.

<img src="https://raw.githubusercontent.com/withanage/OMP_KNV_Plugin/master/static/images/readme/figure2.png">

If the metadata has not been yet sent to KNV, you can click on a hyperlink leading to another page where you can complete several data fields (figure 2). As you can see, there are different kinds of fields, as for example fields where you have to choose among different predefined answers or fields where have to upload PDF files. Then, you can check whether you have filled in all information correctly. For instance, the ISBN number must consist of 13 digits. If someone enters only 12 digits, the input is not valid and the Metadata-Export Tool will show this to you (figure 3).

<img src="https://raw.githubusercontent.com/withanage/OMP_KNV_Plugin/master/static/images/readme/figure3.png">

### ONIX-XML export
 
Screenshot von Link einfügen

### KNV-XML export

Screenshot von Link einfügen
