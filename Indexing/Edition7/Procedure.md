---
purpose: how to use the software
author: m4sterbunny@gmail.com
notes: PDF index generator has a user interface that allows a great deal of functionality, however, there are some techniques that are quicker if they are done in 'code'. This is a mixed-methods approach, using both the interface and uploading files.
---


# PDF index Generator How To

## Getting the settings right

### Advanced Page Numbers (PDF index generator Step 1)

Step 1 allows the pdf to be selected and has the Advanced Page Numbers option:
![image of software step 1](https://github.com/m4sterbunny/ParasitesWithoutBorders/blob/master/images/Step1_PageNumbers.png)

This advanced page numbers option allows the removal of text or editing of the Roman numerals by hand:
NB if the software does not pickup all the front matter- use this as an opportunity to add the Roman numerals (and the knock -on to this is that you have to remove same number of pages to end- when it is all good page number will format green on GUI).
![image of advanced page numbers](https://github.com/m4sterbunny/ParasitesWithoutBorders/blob/master/images/Step1_AdvancedPageNumbers.png)
### Exclude pages (PDF index generator Step 1)
For Edition 7 the decision was to index all pages except front matter and table of contents, and FULL reference pages
* choose index specific pages and exclude pages
* input ranges of pages to exclude in pop up box "Exclude pages"
![image of exclude page numbers](https://github.com/m4sterbunny/ParasitesWithoutBorders/blob/master/images/exclude_pages_%20step_1.png)
    


### Choosing the words to include (PDF index generator Step 2)

Step 2 allows one to select which words and terms to index. The approach we have taken is to create 3 files:

Base terms and variants (e.g. Giardia lamblia is the base term and the variant G. lamblia is merged with that).
Headings and Subheadings
Names

The decision tree for this is handled in a different how to.

This step requires that we use the include words option:
![step 2 including words](https://github.com/m4sterbunny/ParasitesWithoutBorders/blob/master/images/Step2_Words.png)

The UI is intuitive > import option allows you to upload your list (categories/queries). 
![Import Terms](https://github.com/m4sterbunny/ParasitesWithoutBorders/blob/master/images/Step2_Words_Import.png)

NB the software is a little buggy in that if the process has already been driven once you may need to re-upload a list to be able to proceed.
![step 2 adding word lists](https://github.com/m4sterbunny/ParasitesWithoutBorders/blob/master/images/Step2_Include_Words.png)

* Select the "queries/categories" (word lists) to include

* Select "index those words only" to force this restriction

NB For Edition 7 we did not take the plural words option, relying instead on the word list to include all relevant plurals and with the issue that plurals of scientific terms are often not the simple addition of an s. It would be interesting to run both and see how the outcomes differ.

#### Choosing the settings (Step 3)

There are 2 paths to this option, choose "Generate Index Settings" from step 2 or adjust settings from Tools at any stage.

![Tools>Settings](https://github.com/m4sterbunny/ParasitesWithoutBorders/blob/master/images/Settings1.png)

* Enable ignore case sensitivity 
NB this is a lesser of 2 evils option(case sentitivity has been handled in the include words e.g. variants Bee and bee are already included), but some terms were being missed. Enabling this option results in duplicate page numbers- we have some python to clean this up.
* Group consecutive page numbers 
* Ensure "read the visual text of the book" is disable
* Disable "group consecutive page numbers"
    * need single numbers to remove duplicates, but pages will be grouped after duplicates are removed by the Python script.

![Settings>Words to be read](https://github.com/m4sterbunny/ParasitesWithoutBorders/blob/master/images/generate_index_settings_no_page_group.PNG)

### Generate the index (Step 4)

The flow is intuitive to generate the index. With Edition 7 on a mid-level laptop this takes approx 10 minutes.
There are a number of post-processing issues to curate the final list.

# Post-processing of the results (Step 5- PDF Index Generator Step 3)

### Formating Names

The find option allows you to hone in on specific results that arose from queries (lists) that were uploaded as included terms in Step 2.

![Post_Processing_Names](https://github.com/m4sterbunny/ParasitesWithoutBorders/blob/master/images/PostProcessing1.png)

By using the "Find" option and selecting "By include category" you can filter the results down to the hits from a specific list:

![Post Processing Filter](https://github.com/m4sterbunny/ParasitesWithoutBorders/blob/master/images/Post_Processing2.png)

* select ALL of the hits (crtl+A or cmd+A whist cursor is on the grey background)
* select the names query
* format how names are handled using the Aa button:
![Post_Processing Names](https://github.com/m4sterbunny/ParasitesWithoutBorders/blob/master/images/Post_Processing3.png)
* Select the "Deal as name format 2 option" for Last Name, First Name
The software handles all middles names as Last Name, First Name, Middle Names
* check for edge cases such as John de Beer as these will have to be curated by hand where the software will have made it Beer, John de when it should be de Beer, John
    * Carl von Siebold, Ernst von Siebold,  Erwin von Baelz, Antonie van Leeuwenhoek, Jean de Brie, Nicolas Andry de Boisregard, Piraja de Silva

NB This filter must be removed to return the full list for export
![Post Processing Remove Filter](https://github.com/m4sterbunny/ParasitesWithoutBorders/blob/master/images/Post_Processing4.png)

### Check Words Not Found

It may be that edits to the book's text result in a term no longer existing and hence a valid "word not found". More problematic are any false negatives, words that exist in the text and are not found. With all settings adjusted correctly (such as not reading the book as visual text (Step 3)) hyphenated words can be picked up, therefore any other missing words may indicate an issue.

![Post Processing Not Found](https://github.com/m4sterbunny/ParasitesWithoutBorders/blob/master/images/Post_Processing5.png)

* Select "Not Found Words"

To remove the filters select the "show all" option.

### Merge duplicates
* Select the merge duplicates icon from the toolbar
* Check final word is correct
* words that should not be merged can be removed from the merge list with the "-" on the right hand sid
* **Note:** word type is not preserved during merging so if the word was a header it will lose its subheaders so this step should be done before creating headers and subheaders 
![Merge Duplicates](https://github.com/m4sterbunny/ParasitesWithoutBorders/blob/master/images/merge_duplicates_step3.png)

### Assign subheaders to headers
* Right-click on word to access edit word
* Choose word type: Header

![Make word header type](https://github.com/m4sterbunny/ParasitesWithoutBorders/blob/master/images/edit_word_header_step3.png)

* Right-click on word to access "Subheaders..."
* Use search box to find words to add as subheaders and select relevant words

![Select subheaders to add to headword](https://github.com/m4sterbunny/ParasitesWithoutBorders/blob/master/images/add_subheaders_to_headword_step3.png)

* Note: subheaders can be assigned to headers as a query in step 2 however this creates duplicates if the base term is also in the merge query

### Export Index (Optional Step 5)

To assist with issues it is then possible to export the index with each word's status. 

Alternatively the index may be written directly to the pdf (however note this flow has not handled formatting of index for this, also with grouped page numbers the active link option would not be available, where clicking on the entry takes the reader to correct part of pdf).

Assuming an export is needed use the W+arrow button.

![Post Processing Export](https://github.com/m4sterbunny/ParasitesWithoutBorders/blob/master/images/Post_Processing6_Export.png)


![Post Processing Export](https://github.com/m4sterbunny/ParasitesWithoutBorders/blob/master/images/Post_Processing7_Export.png)

### Write the Index (Step 6 - PDF index generator Step 4)

The choice depends upon your needs. If this is the final stage for the indexing, create a text file to later paste into inDesign or MS Word etc. If the setup itself is requred the pdf index generator project will provide a file to recreate aspects of this flow (NB this file does not contain the original term lists and does not recreate all the settings as per these steps).

* Choose colon as the separator for Python script to recognise where the page numbers start
![Writing Index choose separator](https://github.com/m4sterbunny/ParasitesWithoutBorders/blob/master/images/choose_separator_step_4.png)

* export as text file to be used in Python script
![Writing Index Options](https://github.com/m4sterbunny/ParasitesWithoutBorders/blob/master/images/write_index_to_text_step4.png)

## Python clean-up
### Remove duplicate page numbers
* Python scripts are in the ParasitesWithoutBorders repo however to avoid the need to install Python the script has been set up on Google Colaboratory.
    * remove_duplicate_pages_text.ipynb needs to be opened on Google Drive

**Steps**
1. upload the index.txt file generated by PDF index generator into **My Drive** on your Google Drive.
2. Open remove_duplicate_pages_text.ipynb with Colaboratory on your Google Drive. Click on the buttn below.
   ![Open ipynb on google drive](https://github.com/m4sterbunny/ParasitesWithoutBorders/blob/master/images/open_with_colab.png)
3. Press the play button on the first cell to authorize access to your drive 
    * choose the Google account where the index.txt file is saved
4. The next cell "EDIT FILE NAMES and FRONT MATTER" is where you can edit the names of the files and how many roman numeral pages there are.
    * The file path must start with "/content/gdrive/"
    * the full file path will look like this: '/content/gdrive/My Drive/index.txt'
    * If you have saved the file in a different folder you will have to edit the path
        * eg: '/content/gdrive/My Drive/Parasites/index.txt'
    * If there are more than 12 pages of front matter more roman numerals need to be added
5. Press the play button for "EDIT FILE NAMES and FRONT MATTER" cell
6. Press the play button for the last cell
    * Choose where to save the clean index file    
    * A clean_index.txt file will be generated with the format:
    ~~~~
    term1: 67, 89, 90
    term2: 45, 78-82, 100
    ~~~~









