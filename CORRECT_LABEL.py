import json

def opening_translations ():
    while True:
        file = input()
        try:
            json_translation = open(file).read()
            break
        except FileNotFoundError:
            print('something went wrong, '
                  'please check if you typed the name correctly and if the file is saved at your computer '
                  'then type the name of file again')

    translation = json.loads(json_translation)
    return translation


def finding_untranslated_and_missing (first_translation, second_translation):
    untranslated_label=0
    missing_label=0
    good_translated_label={}
    all_wrong_labels_dictionary={}

    for key in first_translation:
        if key not in second_translation:
            missing_label+=1
            all_wrong_labels_dictionary[key] = [first_translation[key],'   ','MISSING']
        elif first_translation[key]==second_translation[key]:
            untranslated_label+=1
            all_wrong_labels_dictionary[key]=[first_translation[key],'   ','UNTRANSLATED']
            del second_translation[key]
        else:
            good_translated_label[key]=second_translation[key]
            del second_translation[key]

    for key in second_translation:
        all_wrong_labels_dictionary[key] = ["   ", second_translation[key], 'DELETED']

    with open('good_translated_labels.txt','w') as outfile:
        json.dump(good_translated_label,outfile)

    print('\nWe found',missing_label,"missing labels\n"+
          'and',untranslated_label,'untranslated labels\n')
    print('Also the program found that something is probably wrong with',len(second_translation),"of labels.\n"
          "Program didn't find this labels in english translation.\n")
    return all_wrong_labels_dictionary


#MAIN PROGRAM
print("Hello, this application will help you check your translations of labels.\n"
      "Please type the name of file which is in english, and then the name of file which you want to check.\n"
      "Please keep in mind that you have to type whole name of files and they have to be json's file.\n")

print('name of first file:')
first_translation=opening_translations()
print('name of second file:')
second_translation=opening_translations()

all_wrong_labels_dictionary=finding_untranslated_and_missing(first_translation,second_translation)

with open('output_labels.csv','w') as f:
    f.write('LABEL,ENG TRANSLATION,ANOTHER TRANSLATION,STATUS\n')
    for key, value in all_wrong_labels_dictionary.items():
        f.write('{0},{1},{2},{3},\n'.format(key,value[0],value[1],value[2]))

print('Program saved all missing and untranslated labels in file output_labels.csv at your computer.\n'
      'Please find the file, and follow instructions from README.txt\n')
print('Thanks for using application and have a nice work :)')
