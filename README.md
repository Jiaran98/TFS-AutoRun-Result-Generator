# TFS-auto-test-result-.trx-file-convertor

#### Why do we need this project?
Creating an error list manually is not intuitive and effective. Since the info in *.trx is massive, you have to massage the data. Therefore, we need a converter to automatically collect the information for us.
#### What does it do?
This tool converts *.trx file to *.xlsx. 
#### How to start?
A simple GUI with three buttons and one input box is available for Windows users.
1. Open button brings up a file explorer. Once you pick *.trx file, the path of it will show up underneath the button.
2. Save button brings up a file exploere, you can select a folder where you want to save *.xlsx.
3. Input Box: Input Name of *.xlsx
4. Run button runs the convertor
##### or:
Use termial:
> python3 AutoRunResultGenerator.py 


### Required Packages:
> pandas
 To get package, please go to https://pandas.pydata.org/
> numpy
 To get package, please go to http://www.numpy.org/
> xlsxwriter
  More information related to xlsxwriter can be found at https://xlsxwriter.readthedocs.io/
