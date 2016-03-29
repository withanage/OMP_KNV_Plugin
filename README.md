# Metadata-Export Tool

The print-on-demand service of KNV (Koch, Neff & Volckmar GmbH) requires for each monograph four files: 
* 1 PDF file containing the cover page
* 1 PDF file containing the content of the monograph
* 1 XML file in the ONIX data format containing metadata
* 1 XML file in a local scheme, defined by KNV, containing metadata

Adminisation and maintenance of metadata can be realised by the use of the Open Monograph Press (OMP). Since OMP is not able to export ONIX- and KNV-XML files, it is necessary to create a tool which can provide those files. The Metadata-Export Tool reads metadata entered into OMP and converts it into the two XML formats required by KNV. Due to the fact that

## Requirements

Following requirements are necessary for the use of the Metadata-Export tool:

* the Python programming language ([version 2.7](https://www.python.org/download/releases/2.7/)) 

* the Python framework [web2py](http://www.web2py.com/init/default/download)

* the database [MySQL](https://www.mysql.de/downloads/), based on OMP

## Technologies

Following technologies and software are used in the development of the Metadata-Export tool: XML, ONIX, web2py and Markdown.

### XML

[XML](https://en.wikipedia.org/wiki/XML) (Extensible Markup Language) is a text-based data format for exchanging hierarchically structured information. The main advantages of XML are easy-readability, simplicity of the syntax and easy adaptability with standardised processing models.

### ONIX

[ONIX](http://home.bic-media.com/index.php/onix-2-1) (Online Information Exchange) is an XML-based data format found by  [EDItEUR](http://www.editeur.org/83/Overview/), an  international organization coordinating development of the standards in e-commerce. ONIX data format is used to exchange bibliographic and product information among publishers, booksellers (e.g. [Amazon.com, Inc.](http://www.amazon.com/books-used-books-textbooks/b?ie=UTF8&node=283155)), libraries and other stakeholders in the book trade.

### web2py

The open source framework [web2py](http://web2py.com/books/default/chapter/29/01/introduction), written in the Python programming language, is used for the development of database-based software. The Python framework web2py includes all the components which are needed to build fully functional web applications.

### Markdown

[Markdown](https://guides.github.com/features/mastering-markdown/) is a simplified and easily readable markup language. Texts written in the Markdown language can be automatically converted into other text formats such as PDF, HTML and MS-Word.

## User Manual

### ONIX-XML export

### KNV-XML export

