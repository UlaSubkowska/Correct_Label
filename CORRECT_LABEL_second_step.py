import csv
import json

print('Hello, nice to see you again!\n'
      'Last time I saved at your computer the txt file which contain all labels which was '
      'correctly translated, please find the exact path of good_translated_labels.txt\n')
print('Type the exact path and name of good_translated_labels.txt file')

while True:
    file = input()
    try:
        json_good_translated = open(file).read()
        break
    except FileNotFoundError:
        print('something went wrong, '
              'please check if you typed the name correctly and type the name of file again')
all_corrected_translations = json.loads(json_good_translated)

print("Please type the exact path and name of file you've corrected (output_labels_corrected.csv)")
while True:
    output_labels = input()
    try:
        with open(output_labels, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                row = row[0].split(';')
                all_corrected_translations[row[0]] = row[2]
        break
    except FileNotFoundError:
        print('something went wrong, '
              'please check if you typed the name correctly and type the name of file again')

del all_corrected_translations['LABEL']

with open('all_corrected_translations.json', 'w') as outfile:
    json.dump(all_corrected_translations, outfile)

print("\nOk it's the end :) program created the file all_corrected_translations.json, so you can find it at your computer and send it to your boss.\n"
      "Remember to attache also the first json file with english translations (example: translations_en_US.json)\n"
      "Have a nice day and see you soon :)")
input()

