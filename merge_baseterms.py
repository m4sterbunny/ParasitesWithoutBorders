'''NOTES:
- the text file should be in the same folder as the Python script
'''
# the names of the input and output files can be changed here
base_terms = "BaseTerms_v8_for_merging.txt"
merged_base_terms = 'baseword_query_v8.txt'

# Read txt file, with/as closes safely if error occurs
with open(base_terms, "r") as file:
    baseword_dict = dict()
    for line in file:
        if line[0].isalnum():
          # make line a key for dict with an empty list
          key = line.strip(' \n')
          key = key.strip('\t')
          baseword_dict[key] = []
          #baseword_dict[key] = [key]
        else:
            line = line.strip(' \n')
            line = line.strip('\t')
            baseword_dict[key].append(line)
#print(baseword_dict)
