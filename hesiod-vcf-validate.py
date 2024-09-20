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
vcf_json_str = libjson.populate_var_from_json_file(os.getcwd(), inputparams[1])
vcf_json_py = libjson.load_json_variable(vcf_json_str)
this_script_name = os.path.basename(__file__)

# Hesiod Header and Log init
liblog.hesiod_print_header()

# Local functions
def validate_vcf(vcf_json_py, md_script_name):
    script = mdlib.get_validate_vcf_md_script(vcf_json_py)
    mdlib.write_cmd_to_script_file(script, md_script_name)

validate_vcf(vcf_json_py, inputparams[2])
print("Your MD configuration file is ready.")
print("File name: "+inputparams[2])