# Import Hesiod libraries
from hesiod import lib_general as libgen
from hesiod import lib_json as libjson
from hesiod import lib_logs_and_headers as liblog 
from hesiod import lib_paramiko as libpko 

# Import VCF libraries
from lib import markdown as mdlib
from lib import excel as xlslib

# Import Standard Python libraries
import os
import sys

# Import vcf parameters workbook json 
vcf_param_workbook_json_str = libjson.populate_var_from_json_file("json", "vcf-param-workbook.json")
vcf_param_workbook_json_py = libjson.load_json_variable(vcf_param_workbook_json_str)

# Get args
inputparams = sys.argv
version = "5.2" #Hardcoded until VCF9

# Import json configuration parameters
this_script_name = os.path.basename(__file__)

# Hesiod Header and Log init
liblog.hesiod_print_header()

# Local functions
def help_stdout():
    print("HELP MENU: hesiod-vcf-validation.py [options]")
    print("Enter options 1x per run, do not add all parameters at once!")
    print("--help option to see this menu.")
    print("")
    print("--xls option to convert the VCF Prerequisites Spreadsheet to VCF JSON file.")
    print("Syntax: --xls <existing VCF Prereq Workbook> <vcf json file to be created>")
    print("")
    print("--md option to convert a VCF JSON file into a structured Markdown file.")
    print("Syntax: --md <existing vcf json file> <markdown filename to be created>")
    print("")
    print("")

def match_help(args):
    if '--help' in args:
        return True

def match_md(args):
    if '--md' in args:
        return True
def match_xls(args):
    if '--xls' in args:
        return True
    
def convert_json_to_markdown(inputparams):
    vcf_json_str = libjson.populate_var_from_json_file(os.getcwd(), inputparams[2])
    vcf_json_py = libjson.load_json_variable(vcf_json_str)
    script = mdlib.get_validate_vcf_md_script(vcf_json_py)
    mdlib.write_cmd_to_script_file(script, inputparams[3])

def convert_xls_to_json(inputparams, vcf_param_workbook_json_py, version):
    # Get list of sheets from vcf-param-workbook.json (important because workbook changes by vcf version)
    sheets_from_xls = xlslib.get_sheets_from_xls(vcf_param_workbook_json_py, version)
    # For each sheet get the json
    sheets_from_xls_as_json_str = []
    sheets_from_xls_as_json_py = []
    for sheet in sheets_from_xls:
        json_str_from_xls = xlslib.get_json_str_from_xls(inputparams, sheet)
        sheets_from_xls_as_json_str.append(json_str_from_xls)
        json_py_from_xls = libjson.load_json_variable(json_str_from_xls)
        sheets_from_xls_as_json_py.append(json_py_from_xls)
    # Get important cells from the workbook and populate VCF json
    new_vcf_json_py = xlslib.vcf_5_2_magic(sheets_from_xls_as_json_py)
    # Write VCF json to file
    libjson.dump_json_to_file(new_vcf_json_py, inputparams[3])
    

# Match args
match_found = False 
match_found = match_help(sys.argv)
if match_found :
    help_stdout()
    sys.exit() 

else:
    match_found = False 
    match_found = match_md(sys.argv)
    if match_found :
        convert_json_to_markdown(inputparams)
        print("Your MD configuration file is ready.")
        print("File name: "+inputparams[3])

    match_found = False 
    match_found = match_xls(sys.argv)
    if match_found :
        convert_xls_to_json(inputparams, vcf_param_workbook_json_py, version)
        print("")
        print("Your JSON configuration file is ready.")
        print("File name: "+inputparams[3])

