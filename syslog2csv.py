#!/usr/bin/env python
import getpass
import os.path

global username
username = getpass.getuser()

def SYSLOGTYPINPUT():
    '''
    Ask the User fot the Typ of syslog
    '''
    systyplist = ('1 = rsyslog',
                  '2 = Qnap (Not Ready)',
                   '3 = Synology (Not Supported)',
                   '4 = Syslog-ng (Not Supported)',
                   '5 = Kiwi (Not Supported)',
                  )
    syslogtyp = '' # name of the syslog type
    while syslogtyp == '':
        print('List of Syslog Server')
        print('-------------------------')
        for i in systyplist:
            print(i)
        print('-------------------------')
        syslogtyp = raw_input('Typ Number of syslog ? [No Default]  ')

    if (syslogtyp < '1' or syslogtyp > '5'):
        print('==============================================')
        quit('error: wrong type of syslog')

    if (syslogtyp == '2' or syslogtyp == '3' or syslogtyp == '4' or syslogtyp == '5'):
        print('==============================================')
        quit('error: sorry Syslog Typ not Supported at the moment!')

    return(syslogtyp)

def FINPUT():
    '''
    Ask the User for the Path + Name of the syslog file
    '''
    finputpath = raw_input('Path to syslog file [/var/log/]: ')

    if finputpath == '':
        finputpath = '/var/log/'

    finputname = raw_input('Name of syslog file [syslog]: ')

    if finputname == '':
        finputname = 'syslog'

    finput=finputpath+finputname

    return(finput)

def FOUTPUT():
    '''
    Ask the User where to save the CSV file
    '''
    foutputpath = raw_input ('Path to save csv file [/home/'+username+'/]: ')

    if foutputpath == '':
        foutputpath = '/home/'+username+'/'

    if foutputpath.endswith('/'):
        pass
    else:
        foutputpath = foutputpath+'/'

    foutputname = raw_input ('Name of csv file [syslog_1.csv]: ')

    if foutputname == '':
        foutputname = 'syslog_1.csv'

    while os.path.isfile(foutputpath+foutputname):
        fcheck = raw_input ('Overwrite File '+foutputname+' (Y/N)? [Default=N]  ')
        if (fcheck == 'N' or fcheck =='n' or fcheck == ''):
            foutputname = raw_input ('Put in new filename for csv file [syslog_2.csv]: ')
        if (fcheck == 'Y' or fcheck == 'y'):
            break
        if foutputname == '':
            foutputname = 'syslog_2.csv'

    foutput=foutputpath+foutputname

    return(foutput)

def RSYSLOG(finput,foutput):
    '''
    Funktion for converting rsyslog log files
    '''
    n = 4   # how many spaces to remove
    ic = 5   # where to add \n
    # read in syslog file and write it into list
    with open(finput) as f:
        raw_file_input = f.read().splitlines()
    # remove spaces from list
    raw_file_output = []
    for len in raw_file_input:  # for every entry in variable
        raw_file_output.extend(len.split(' ' , n))  # remove space
    # insert \n
    c1 = 0 # counter 1
    c2 = 1 # couner 2
    c3 = 0 # counter 3
    for ele in raw_file_output:
        c1 += 1
        if c1 == c2*ic+c3:
            raw_file_output.insert(c2*ic+c3, '\n')
            c2 += 1
            c3 += 1
    # write csv file
    fieldnames = ['Month', 'Day', 'Time', 'Hostname', 'Message\n']
    f = open(foutput, "w")
    for ele in fieldnames:
        f.write(';'+ele)
    for ele in raw_file_output:
        f.write(';'+ele)
    return

def QNAP(finput,foutput):
    '''
    Funktion for converting qnap log files
    '''
    n = 3   # how many spaces to remove
    ic = 4  # where to add \n
    # read in syslog file and write it into a string
    f = open(finputpath+finputname)
    raw_file_input1 = f.read()
    raw_index = [m.start() for m in re.finditer(r'{}'.format(re.escape('+02:00')), raw_file_input1)]
    [0, 6]
    raw_file_output1 = []
    for ele in raw_index:
        raw_file_output1
    raw_file_output1.insert(0,raw_file_input1)

def main ():

    print('==============================================')
    print('Hello '+username+' here are some infos for you!')
    print ('I need a few inputs to work properly!')
    print ('For default input just press enter')
    print('==============================================')

    syslogtyp = SYSLOGTYPINPUT()
    finput = FINPUT()
    foutput = FOUTPUT()

    #rsyslog
    if syslogtyp == 'rsyslog':
        RSYSLOG(finput,foutput)

    #qnap
    if syslogtyp == 'qnap':
        QNAP(finput,foutput)

    print('\n==============================================')
    print('Finished converting\nSaved file under '+foutput)
    raw_input('Press enter to exit.\n')

if __name__ == "__main__":
   try:
      main()
   except KeyboardInterrupt:
      print '\n' # do nothing here
      pass
