This is a file for keeping our brains straight for indexing
# Preparing text files for indexing
## BaseTerms
* baseterms_for_merging.txt
* Words which should be a head or subhead word are not annotated in this text file.  All the derived words will be merged with the base word from this document. 

* The words are given in the following format:
  
~~~~
Base word
	Derived word 1
	Derived word 2
~~~~

**Note:** the tab before the derived words is needed by the Python script to identify it as a derived word of the previous un-tabbed word, extra lines between sets of base words and their derivatives

The  Python script will output a text file that can be used as a query in PDF Index generator. The form for merging words is as follows:

`Base + D1 + D2 = Base` ( or any word that you want to be the displayed word)
**Note:**
List is in alphebetical order except some for sometimes when the words will become subheadings(for now)
e.g. 
~~~~~
ascariasis 	
	Ascariasis	
hepatobilary ascariasis 	
	Hepatobiliary ascariasis	
pancreatic 	
neonatal ascariasis 
	Neonatal ascariasis
~~~~

# Indexing Process
**Note:** Can only have one project file open at a time for pdf index generator
## Step 1
1.	Browse for pdf file
2.	Choose index all pages 
3.	Click on Advanced page numbers
      * Edit pages to match print version Roman numerals for preface etc. (NB can remove F from front matter by hand)
4. Click on *TEXT* (bottom right button)
5. May get a warning about allocating more memory (i.e. RAM) 
    * click **Yes**

## Step 2: Index Generation Options
1.	Click on Generating Index settings to set up categories etc.
    * Settings box will pop up
2.	In Settings box click on + Include words
    * Import text files to make categories
      * merged_basewords
      * headers with subheaders
      * names
3. In Tools > Settings box Generating Index
  * Disable the option "Read the visual text of the book".
      * this is so it will recognize hypenated words
4. Click Ok to save settings
5. Choose Index specific words
    * click on **+ Include words**
    * choose categories to include (these are the ones we set up above)
      * merged, headers, names
    * Tick box that says **Index those words only**
    * click ok
6. Click generate index (bottom right)
    * this process can take a while, up to 10 min
    * click done
  

## Step 3: Edit index results table
### Names
1.We highlight all names in the table, click the “Format” button found on the toolbar, and click “Deal as a name – Format 2”. That will automatically invert all names to appear as Last Name, First Name.
### Checks
1. Check words not found
2. 

### Settings
1. Editing index
	* Manage word labels
		* allows you to group types of words together e.g. names
		

## Step 4
1.	Choose settings
	  * Append to original (little tick on left side)
	  * Separate pdf index and/or text file index
2.	Click on Writing Settings
	  * Choose style, fonts etc
	  * Choose to display page numbers for header words (checkbox)

 


