# Function to make page ranges
def formatpagelist(numberlist):
    prev_number = min(numberlist) if numberlist else None
    pagelist = list()

    for number in sorted(numberlist):
        if number != prev_number+1:
            pagelist.append([number])
        elif len(pagelist[-1]) > 1:
            pagelist[-1][-1] = number
        else:
            pagelist[-1].append(number)
        prev_number = number

    return ', '.join(['-'.join(map(str,page)) for page in pagelist])


# the names of the input and output files can be changed here
dirty_index = "preclean_20190424.txt"
clean_index = 'clean_index_20190424.txt'
# list all roman numerals here (currently up to 12)
front_matter = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi", "xii"]

# Read txt file, with/as closes safely if error occurs
with open(dirty_index, "r") as file:
    word_dict = dict()
    for line in file:
        line = line.strip("\n")
        word_pages = line.split(":")
        key = word_pages[0]
        pages_list = word_pages[1].split(", ")

        # Remove duplicates
        clean_pages = []
        for item in pages_list:
            # only add page if not in list
            if item not in clean_pages:
                clean_pages.append(item)

        roman_list = []
        int_pages = []
        for item in clean_pages:
            if item in front_matter:
                roman_list.append(item)
            else:
                int_pages.append(int(item))

        # Roman numeral pages in front matter
        roman_pages = str()
        for page in roman_list:
            roman_pages += "{p}, ".format(p=page)
        # Format so pages separated by a comma or made into a range
        pages = formatpagelist(int_pages)

        # Add Roman numerals to integer page numbers
        if roman_list == []:
            word_dict[key] = pages
        else:
            word_dict[key] = roman_pages + pages

# Make a new file with clean index
with open(clean_index, 'w')as file:
    key_list = word_dict.keys()
    index_lines = str()
    for key in key_list:
        index_lines += "{word}: ".format(word=key)
        index_lines += "{p}\n".format(p=word_dict[key])

    file.write(index_lines)
    # print(index_lines)

