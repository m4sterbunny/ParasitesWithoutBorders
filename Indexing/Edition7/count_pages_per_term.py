#modified clean index script to count how many pages or page ranges are listed for each term

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
count_pages = "count_pages.txt"

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

        front_matter = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi", "xii"]
        roman_list = []
        int_pages = []
        for item in clean_pages:
            if item in front_matter:
                roman_list.append(item)
                # print (roman_list)
            else:
                int_pages.append(int(item))

        pages = formatpagelist(int_pages)
        if roman_list == []:
            word_dict[key] = pages
        else:
            #print(roman_list)
            word_dict[key] = roman_list[0] + ", "+ pages

# Make a new file with clean index
with open(count_pages, 'w')as file:
    key_list = word_dict.keys()

    page_count_lines = str()
    for key in key_list:
        final_list = word_dict[key].split(", ")
        count = 0
        for item in final_list:
            count += 1
        if count > 20:
            page_count_lines += "{word}: ".format(word=key)
            page_count_lines += "{c}\n".format(c=count)
    #print (page_count_lines)
    file.write(page_count_lines)
