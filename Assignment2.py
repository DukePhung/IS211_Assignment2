from urllib import request
import logging

birthdays = 'http://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv'

LOG_FILENAME = 'Assignment2_logs.out'
logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.DEBUG)


def downloadData(csv_url):
    """Access csv file from URL and write to local csv file.

    Args:
        csv_url (link): link where the csv file is located

    Returns:
        file: csv file that contains all information on URL.
    """

    response = request.urlopen(csv_url)
    csvfile = response.read()
    csv_str = str(csvfile)
    lines = csv_str.split("\\n")
    dest_url = r'csvData.csv'
    fx = open(dest_url, 'w')

    for line in lines:
        fx.write(line + '\n')

    fx.close()

    return dest_url


def processData(myfile):
    """Retrieves stored csv file and append to dictionary.

    Args:
        myfile (csv): csv file that contains data

    Returns:
        mydict: dictionary with ID as key, with name and birthday as value.
    """

    with open(myfile, 'r') as csv_file:

        for row in csv_file:
            values = row.split(',')
            mydict[values[0]] = values[1:]

    return mydict


def displayPerson():
    """Continuing loop to retrieve name and birthday from input key."""

    answer = 'yes'

    while answer != 'no':
        info_request = input('Please input ID number or type exit to quit: ')
        if info_request == 'exit':
            break
        else:
            try:
                print(mydict[info_request])
            except KeyError:
                logging.debug("Requested ID {} not found".format(info_request))
                print('Requested ID {} not found!'.format(info_request))
        answer = input('Would you like to search again, enter yes or no: ')


if __name__ == "__main__":
    mydict = {}
    downloadData(birthdays)
    processData('csvData.csv')
    displayPerson()
