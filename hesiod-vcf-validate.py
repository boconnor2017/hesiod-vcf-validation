# Import Hesiod libraries
from hesiod import lib_general as libgen
from hesiod import lib_json as libjson
from hesiod import lib_logs_and_headers as liblog 
from hesiod import lib_paramiko as libpko 

# Import VCF libraries
from lib import markdown as mdlib

# Import Standard Python libraries
import os
import sys

# Get args
inputparams = sys.argv

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

def convert_xls_to_json(inputparams):
    print("Coming soon...")

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
        convert_xls_to_json(inputparams)
        print("Your JSON configuration file is ready.")
        print("File name: "+inputparams[3])

