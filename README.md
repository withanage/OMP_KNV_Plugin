# Metadata-Export Tool

This tool exports metadata files for the print-on-demand (POD) service of [KNV](http://www.knv.de/lieferanten.html) (Koch, Neff & Volckmar GmbH).The POD service demands for each monograph/edited volume four different files: 
* 1 PDF file containing the cover page
* 1 PDF file containing the content of the monograph
* 1 XML file containing metadata (ONIX-XML format) 
* 1 XML file containing metadata (local XML scheme defined by KNV)

In our use case, administration and maintenance of metadata is done in the [Open Monograph Press](https://pkp.sfu.ca/omp/) (OMP). Since OMP is not able to export ONIX- and KNV-XML formats as defined by KNV, the Metadata-Export Tool reads metadata entered into OMP and converts it into the two XML formats required by KNV. The tool provides extra form-based input masks for metadata which can not be entered into OMP.

The Metadata-Export Tool is web-based and able to export XML files.

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

Figure 1 shows the index page of the Metadata-Export Tool. In the navigation menu, you can choose whether you want to see a list of published or unpublished books. In both cases, the monographs are listed in a table and sorted by their descending submission ID. The table of unpublished books (figure 1) consists of four columns.
Those columns are: 
* submission ID
* setting value (title) 
* date submitted
* status

The status column shows the user whether the metadata has already been sent to KNV or not. If the metadata has not yet been sent to KNV, you can click on the hyperlink leading to a metadata entering page for KNV (figure 2). 

<img src="https://raw.githubusercontent.com/withanage/OMP_KNV_Plugin/master/static/images/readme/figure2.png">

In the metadata entering form, there are different kinds of fields: data fields, file upload fields and selection boxes. Data entered into those fields are checked against rules defined by KNV.

<img src="https://raw.githubusercontent.com/withanage/OMP_KNV_Plugin/master/static/images/readme/figure3.png">

E.g. the ISBN number must consist of 13 digits. If someone enters only 12 digits, the input is not valid and the Metadata-Export Tool will return this to you (figure 3).

<img src="https://raw.githubusercontent.com/withanage/OMP_KNV_Plugin/master/static/images/readme/figure4.png">

In the table of published books (figure 4) the column 'status' is replaced by two other columns.
Those columns are:
* KNV-XML
* ONIX

These two columns contain hyperlinks directly leading to the download of the ONIX- and the KNV-XML file. 

### ONIX-XML export
 
<img src="https://raw.githubusercontent.com/withanage/OMP_KNV_Plugin/master/static/images/readme/figure5.png">

Figure 5 shows an example for an ONIX-XML file.

### KNV-XML export

<img src="https://raw.githubusercontent.com/withanage/OMP_KNV_Plugin/master/static/images/readme/figure06.png">

Figure 6 shows an example for a KNV-XML file.
