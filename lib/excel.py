import pandas as pd
import json

# Import Hesiod libraries
from hesiod import lib_general as libgen
from hesiod import lib_json as libjson
from hesiod import lib_logs_and_headers as liblog 
from hesiod import lib_paramiko as libpko 

# Read Excel and select a single cell (and make it a header for a column)
#filename = "vcf-papw-test2.xlsx" # Pass this in as args
#sheetname = "Deployment Options" # Retreieve from json 


'''
# Convert Excel To Json With Python
data = pd.read_excel(filename, sheet_name=sheetname)
json_data_from_excel_file = data.to_json()
json_data_py = libjson.load_json_variable(json_data_from_excel_file)


# Loop through sheet using json

i=0 #Column
y=0 #Row
total_columns = 15
total_rows = 75

while i < total_columns:
    print("Column "+str(i)+": ")
    while y < total_rows:
        print("Row "+str(y)+": ")
        print(json_data_py["Unnamed: "+str(i)][str(y)])
        y=y+1
    i=i+1
    y=0

# Cell Value (H11)
column_number = 7 #H
row_number = 9 #11
cellvalue = json_data_py["Unnamed: "+str(column_number)][str(row_number)]
print(cellvalue)

'''

# Custom
def get_sheets_from_xls(vcf_param_workbook_json_py, version):
    i = 0
    y = 0
    sheets_from_xls = []
    while i < len(vcf_param_workbook_json_py["excelstructure"]):
        if version == vcf_param_workbook_json_py["excelstructure"][i]["version"]:
            while y < len(vcf_param_workbook_json_py["excelstructure"][i]["sheetspecs"]):
                sheetname = vcf_param_workbook_json_py["excelstructure"][i]["sheetspecs"][y]["tabname"]
                sheets_from_xls.append(sheetname)
                y=y+1
        i=i+1
        y=0
    return sheets_from_xls

def get_json_str_from_xls(inputparams, sheet):
    data = pd.read_excel(inputparams[2], sheet_name=sheet)
    json_str_from_xls = data.to_json()
    return json_str_from_xls

def get_netmask(cidr):
    subnet_cheatsheet = []
    subnet_cheatsheet.append({
        "cidr" : "0",
        "subnet" : "0.0.0.0"
    })
    subnet_cheatsheet.append({
        "cidr" : "1",
        "subnet" : "128.0.0.0"
    })
    subnet_cheatsheet.append({
        "cidr" : "2",
        "subnet" : "192.0.0.0"
    })
    subnet_cheatsheet.append({
        "cidr" : "3",
        "subnet" : "224.0.0.0"
    })
    subnet_cheatsheet.append({
        "cidr" : "4",
        "subnet" : "240.0.0.0"
    })
    subnet_cheatsheet.append({
        "cidr" : "5",
        "subnet" : "248.0.0.0"
    })
    subnet_cheatsheet.append({
        "cidr" : "6",
        "subnet" : "252.0.0.0"
    })
    subnet_cheatsheet.append({
        "cidr" : "7",
        "subnet" : "254.0.0.0"
    })
    subnet_cheatsheet.append({
        "cidr" : "8",
        "subnet" : "255.0.0.0"
    })
    subnet_cheatsheet.append({
        "cidr" : "9",
        "subnet" : "255.128.0.0"
    })
    subnet_cheatsheet.append({
        "cidr" : "10",
        "subnet" : "255.192.0.0"
    })
    subnet_cheatsheet.append({
        "cidr" : "11",
        "subnet" : "255.224.0.0"
    })
    subnet_cheatsheet.append({
        "cidr" : "12",
        "subnet" : "255.240.0.0"
    })
    subnet_cheatsheet.append({
        "cidr" : "13",
        "subnet" : "255.248.0.0"
    })
    subnet_cheatsheet.append({
        "cidr" : "14",
        "subnet" : "255.252.0.0"
    })
    subnet_cheatsheet.append({
        "cidr" : "15",
        "subnet" : "255.254.0.0"
    })
    subnet_cheatsheet.append({
        "cidr" : "16",
        "subnet" : "255.255.0.0"
    })
    subnet_cheatsheet.append({
        "cidr" : "17",
        "subnet" : "255.255.128.0"
    })
    subnet_cheatsheet.append({
        "cidr" : "18",
        "subnet" : "255.255.192.0"
    })
    subnet_cheatsheet.append({
        "cidr" : "19",
        "subnet" : "255.255.224.0"
    })
    subnet_cheatsheet.append({
        "cidr" : "20",
        "subnet" : "255.255.240.0"
    })
    subnet_cheatsheet.append({
        "cidr" : "21",
        "subnet" : "255.255.248.0"
    })
    subnet_cheatsheet.append({
        "cidr" : "22",
        "subnet" : "255.255.252.0"
    })
    subnet_cheatsheet.append({
        "cidr" : "23",
        "subnet" : "255.255.254.0"
    })
    subnet_cheatsheet.append({
        "cidr" : "24",
        "subnet" : "255.255.255.0"
    })
    subnet_cheatsheet.append({
        "cidr" : "25",
        "subnet" : "255.255.255.128"
    })
    subnet_cheatsheet.append({
        "cidr" : "26",
        "subnet" : "255.255.255.192"
    })
    subnet_cheatsheet.append({
        "cidr" : "27",
        "subnet" : "255.255.255.224"
    })
    subnet_cheatsheet.append({
        "cidr" : "28",
        "subnet" : "255.255.255.240"
    })
    subnet_cheatsheet.append({
        "cidr" : "29",
        "subnet" : "255.255.255.248"
    })
    subnet_cheatsheet.append({
        "cidr" : "30",
        "subnet" : "255.255.255.252"
    })
    subnet_cheatsheet.append({
        "cidr" : "31",
        "subnet" : "255.255.255.254"
    })
    subnet_cheatsheet.append({
        "cidr" : "32",
        "subnet" : "255.255.255.255"
    })
    i=0
    while i < len(subnet_cheatsheet):
        if subnet_cheatsheet[i]["cidr"] == cidr:
            subnet = subnet_cheatsheet[i]["subnet"]
        i=i+1
    return subnet

def get_value_from_cell(col, row, json_data_py, col_calibrationval, row_calibrationval):
    # col: A=0, B=1, C=2, etc
    # row: use the row number from the spreadsheet
    col = (col+col_calibrationval) #Accounts for hidden columns
    row = (row+row_calibrationval) #Accounts for hidden rows
    value_from_cell =  json_data_py["Unnamed: "+str(col)][str(row)]
    return value_from_cell

def vcf_5_2_magic(sheets_from_xls_as_json_py):
    # This script is customized to work with VCF 5.2 
    # Populate info from Tab 0: "Deployment Options"
    tab = 0
    col_calibrationval = -2
    row_calibrationval = -2
    version = get_value_from_cell(9, 11, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    # Populate info from Tab 2: "Management Domain Sizing Inputs"
    tab = 2
    col_calibrationval = 0
    row_calibrationval = -2
    vcsa_size = get_value_from_cell(4, 25, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    nsxt_manager_size = get_value_from_cell(7, 25, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    # Populate info from Tab 3: "Network Inputs - Rack"
    tab = 3
    col_calibrationval = 0
    row_calibrationval = -2
    management_vm_network_vlan_id = get_value_from_cell(3, 9, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    management_vm_network_subnet = get_value_from_cell(5, 9, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    management_vm_network_gateway = get_value_from_cell(7, 9, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    management_vm_network_mtu = get_value_from_cell(9, 9, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    vmotion_vm_network_vlan_id = get_value_from_cell(3, 11, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    vmotion_vm_network_subnet = get_value_from_cell(5, 11, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    vmotion_vm_network_gateway = get_value_from_cell(7, 11, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    vmotion_vm_network_mtu = get_value_from_cell(9, 11, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    vsan_vm_network_vlan_id = get_value_from_cell(3, 12, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    vsan_vm_network_subnet = get_value_from_cell(5, 12, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    vsan_vm_network_gateway = get_value_from_cell(7, 12, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    vsan_vm_network_mtu = get_value_from_cell(9, 12, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    nsx_host_overlay_vlan_id = get_value_from_cell(3, 13, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    nsx_host_overlay_subnet = get_value_from_cell(5, 13, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    nsx_host_overlay_gateway = get_value_from_cell(7, 13, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    nsx_host_overlay_mtu = get_value_from_cell(9, 13, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    # Populate info from Tab 4: "Name and IP Address Inputs - VM"
    tab = 4
    col_calibrationval = 0
    row_calibrationval = -2
    cloud_builder_hostname = get_value_from_cell(4, 38, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    cloud_builder_ip = get_value_from_cell(6, 38, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    sddc_manager_hostname = get_value_from_cell(4, 39, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    sddc_manager_ip = get_value_from_cell(6, 39, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    vcsa_hostname = get_value_from_cell(4, 40, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    vcsa_ip = get_value_from_cell(6, 40, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    nsx_mgr_hostname = get_value_from_cell(4, 41, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    nsx_mgr_vip = get_value_from_cell(6, 41, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    nsx_mgr_a_hostname = get_value_from_cell(4, 42, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    nsx_mgr_a_ip = get_value_from_cell(6, 42, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    nsx_mgr_b_hostname = get_value_from_cell(4, 43, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    nsx_mgr_b_ip = get_value_from_cell(6, 43, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    nsx_mgr_c_hostname = get_value_from_cell(4, 44, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    nsx_mgr_c_ip = get_value_from_cell(6, 44, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    ntp_servers = []
    ntp_servers.append(get_value_from_cell(3, 9, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval))
    if not(pd.isna(get_value_from_cell(3, 10, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval))):
        ntp_servers.append(get_value_from_cell(3, 10, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval))
    child_dns_zone = get_value_from_cell(3, 18, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    dns_servers = []
    dns_servers.append(get_value_from_cell(3, 20, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval))
    dns_servers.append(get_value_from_cell(3, 21, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval))
    sftp_server = get_value_from_cell(3, 31, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    # Populate info from Tab 5: "Name & IP Address Inputs - Rack"
    tab = 5
    col_calibrationval = 0
    row_calibrationval = -2
    esxi_values_from_xls = []
    esxi_values_from_xls.append({})
    esxi_values_from_xls[0]["hostname"] = get_value_from_cell(3, 9, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    esxi_values_from_xls[0]["ip"] = get_value_from_cell(5, 9, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    esxi_values_from_xls.append({})
    esxi_values_from_xls[1]["hostname"] = get_value_from_cell(3, 10, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    esxi_values_from_xls[1]["ip"] = get_value_from_cell(5, 10, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    esxi_values_from_xls.append({})
    esxi_values_from_xls[2]["hostname"] = get_value_from_cell(3, 11, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    esxi_values_from_xls[2]["ip"] = get_value_from_cell(5, 11, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    esxi_values_from_xls.append({})
    esxi_values_from_xls[3]["hostname"] = get_value_from_cell(3, 12, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    esxi_values_from_xls[3]["ip"] = get_value_from_cell(5, 12, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    # Note: these values may be null - only 4 hosts are required for VCF bringup
    esxi_values_from_xls.append({})
    esxi_values_from_xls[4]["hostname"] = get_value_from_cell(3, 13, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    esxi_values_from_xls[4]["ip"] = get_value_from_cell(5, 13, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    esxi_values_from_xls.append({})
    esxi_values_from_xls[5]["hostname"] = get_value_from_cell(3, 14, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    esxi_values_from_xls[5]["ip"] = get_value_from_cell(5, 14, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    esxi_values_from_xls.append({})
    esxi_values_from_xls[6]["hostname"] = get_value_from_cell(3, 15, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    esxi_values_from_xls[6]["ip"] = get_value_from_cell(5, 15, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    esxi_values_from_xls.append({})
    esxi_values_from_xls[7]["hostname"] = get_value_from_cell(3, 16, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    esxi_values_from_xls[7]["ip"] = get_value_from_cell(5, 16, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    esxi_values_from_xls.append({})
    esxi_values_from_xls[8]["hostname"] = get_value_from_cell(3, 17, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    esxi_values_from_xls[8]["ip"] = get_value_from_cell(5, 17, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    esxi_values_from_xls.append({})
    esxi_values_from_xls[9]["hostname"] = get_value_from_cell(3, 18, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    esxi_values_from_xls[9]["ip"] = get_value_from_cell(5, 18, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    esxi_values_from_xls.append({})
    esxi_values_from_xls[10]["hostname"] = get_value_from_cell(3, 19, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    esxi_values_from_xls[10]["ip"] = get_value_from_cell(5, 19, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    esxi_values_from_xls.append({})
    esxi_values_from_xls[11]["hostname"] = get_value_from_cell(3, 20, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    esxi_values_from_xls[11]["ip"] = get_value_from_cell(5, 20, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    esxi_values_from_xls.append({})
    esxi_values_from_xls[12]["hostname"] = get_value_from_cell(3, 21, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    esxi_values_from_xls[12]["ip"] = get_value_from_cell(5, 21, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    esxi_values_from_xls.append({})
    esxi_values_from_xls[13]["hostname"] = get_value_from_cell(3, 22, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    esxi_values_from_xls[13]["ip"] = get_value_from_cell(5, 22, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    esxi_values_from_xls.append({})
    esxi_values_from_xls[14]["hostname"] = get_value_from_cell(3, 23, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    esxi_values_from_xls[14]["ip"] = get_value_from_cell(5, 23, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    esxi_values_from_xls.append({})
    esxi_values_from_xls[15]["hostname"] = get_value_from_cell(3, 24, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    esxi_values_from_xls[15]["ip"] = get_value_from_cell(5, 24, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    vmotion_pool_start_ip = get_value_from_cell(5, 55, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    vmotion_pool_end_ip = get_value_from_cell(5, 56, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    vsan_pool_start_ip = get_value_from_cell(5, 57, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    vsan_pool_end_ip = get_value_from_cell(5, 58, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    host_tep_overlay_pool_start_ip = get_value_from_cell(5, 59, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    host_tep_overlay_pool_end_ip = get_value_from_cell(5, 60, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    # Populate info from Tab 6: "SDDC Inputs - Common"
    tab = 6
    col_calibrationval = 0
    row_calibrationval = -2
    vcenter_license_key = get_value_from_cell(3, 17, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    esxi_license_key = get_value_from_cell(3, 18, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    vsan_license_key = get_value_from_cell(3, 19, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    nsx_license_key = get_value_from_cell(3, 20, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    esxi_password = get_value_from_cell(3, 28, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    vc_admin_password = get_value_from_cell(3, 30, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    vc_root_password = get_value_from_cell(3, 31, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    nsxm_root_password = get_value_from_cell(3, 33, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    nsxm_admin_password = get_value_from_cell(3, 34, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    nsxm_audit_password = get_value_from_cell(3, 35, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    nsxe_root_password = get_value_from_cell(3, 36, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    nsxe_admin_password = get_value_from_cell(3, 37, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    nsxe_audit_password = get_value_from_cell(3, 38, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    sddcmgr_root_password = get_value_from_cell(3, 43, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    sddcmgr_vcf_password = get_value_from_cell(3, 44, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    sddcmgr_admin_password = get_value_from_cell(3, 45, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    sddcmgr_depot_username = get_value_from_cell(3, 46, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    sddcmgr_depot_password = get_value_from_cell(3, 47, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    sftp_user = get_value_from_cell(3, 55, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    sftp_password = get_value_from_cell(3, 56, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    cloud_foundation_mgt_domain_name = get_value_from_cell(3, 70, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    enable_ceip = get_value_from_cell(3, 75, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    enable_fips = get_value_from_cell(3, 76, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    vsphere_standard_switch_mgt = get_value_from_cell(3, 79, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    vds_name = get_value_from_cell(3, 80, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    vds_pnics = get_value_from_cell(3, 81, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    vds_mtu = get_value_from_cell(3, 82, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    vds_profile = get_value_from_cell(3, 83, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    mgt_vm_network = get_value_from_cell(3, 87, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    vmotion_vm_network = get_value_from_cell(3, 88, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    vsan_vm_network = get_value_from_cell(3, 89, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    vsan_datastore_name = get_value_from_cell(3, 117, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    datacenter_name = get_value_from_cell(3, 122, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    mgt_cluster_name = get_value_from_cell(3, 125, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    mgt_cluster_evc_settings = get_value_from_cell(3, 126, sheets_from_xls_as_json_py[tab], col_calibrationval, row_calibrationval)
    if mgt_cluster_evc_settings:
        mgt_cluster_evc_settings = mgt_cluster_evc_settings
    else:
        mgt_cluster_evc_settings = ""
    # Init the vcf 5.2 json variable
    new_vcf_json_py = {}
    new_vcf_json_py["dvSwitchVersion"] = "7.0.0"
    new_vcf_json_py["skipEsxThumbprintValidation"] = True
    new_vcf_json_py["managementPoolName"] = "bringup-networkpool"
    new_vcf_json_py["sddcManagerSpec"] = {}
    new_vcf_json_py["sddcManagerSpec"]["hostname"] = sddc_manager_hostname
    new_vcf_json_py["sddcManagerSpec"]["ipAddress"] = sddc_manager_ip
    cidr = management_vm_network_subnet[-2:]
    sddc_manager_netmask = get_netmask(cidr)
    new_vcf_json_py["sddcManagerSpec"]["netmask"] = sddc_manager_netmask
    new_vcf_json_py["sddcManagerSpec"]["localUserPassword"] = sddcmgr_admin_password
    new_vcf_json_py["sddcManagerSpec"]["rootUserCredentials"] = {}
    new_vcf_json_py["sddcManagerSpec"]["rootUserCredentials"]["username"] = "root"
    new_vcf_json_py["sddcManagerSpec"]["rootUserCredentials"]["password"] = sddcmgr_root_password
    new_vcf_json_py["sddcManagerSpec"]["secondUserCredentials"] = {}
    new_vcf_json_py["sddcManagerSpec"]["secondUserCredentials"]["username"] = "vcf"
    new_vcf_json_py["sddcManagerSpec"]["secondUserCredentials"]["password"] = sddcmgr_vcf_password
    new_vcf_json_py["sddcId"] = "sddcId-public-api-01" #default - doesnt exist anywhere in the workbook
    new_vcf_json_py["esxLicense"] = esxi_license_key
    new_vcf_json_py["taskName"] = "workflowconfig/workflowspec-ems.json" #default - doesnt exist anywhere in the workbook
    new_vcf_json_py["ntpServers"] = ntp_servers
    new_vcf_json_py["dnsSpec"] = {}
    new_vcf_json_py["dnsSpec"]["subdomain"] = child_dns_zone
    new_vcf_json_py["dnsSpec"]["domain"] = child_dns_zone
    new_vcf_json_py["dnsSpec"]["nameserver"] = dns_servers[0]
    new_vcf_json_py["dnsSpec"]["secondaryNameserver"] = dns_servers[1]
    new_vcf_json_py["networkSpecs"] = []
    new_vcf_json_py["networkSpecs"].append({})
    new_vcf_json_py["networkSpecs"][0]["subnet"] = management_vm_network_subnet
    new_vcf_json_py["networkSpecs"][0]["vlanId"] = management_vm_network_vlan_id
    new_vcf_json_py["networkSpecs"][0]["mtu"] = management_vm_network_mtu
    new_vcf_json_py["networkSpecs"][0]["networkType"] = "MANAGEMENT"
    new_vcf_json_py["networkSpecs"][0]["gateway"] = management_vm_network_gateway
    new_vcf_json_py["networkSpecs"].append({})
    new_vcf_json_py["networkSpecs"][1]["subnet"] = vsan_vm_network_subnet
    new_vcf_json_py["networkSpecs"][1]["includeIpAddressRanges"] = []
    new_vcf_json_py["networkSpecs"][1]["includeIpAddressRanges"].append({})
    new_vcf_json_py["networkSpecs"][1]["includeIpAddressRanges"][0]["startIpAddress"] = vsan_pool_start_ip
    new_vcf_json_py["networkSpecs"][1]["includeIpAddressRanges"][0]["endIpAddress"] = vsan_pool_end_ip
    #Magic to reduce complexity (include IP addresses)
    vsan_subnet = vsan_vm_network_subnet.split(".")
    new_vcf_json_py["networkSpecs"][1]["includeIpAddress"] = []
    new_vcf_json_py["networkSpecs"][1]["includeIpAddress"].append(vsan_subnet[0]+"."+vsan_subnet[1]+"."+vsan_subnet[2]+"."+"50")
    new_vcf_json_py["networkSpecs"][1]["includeIpAddress"].append(vsan_subnet[0]+"."+vsan_subnet[1]+"."+vsan_subnet[2]+"."+"49")
    #End magic (include IP addresses)
    new_vcf_json_py["networkSpecs"][1]["vlanId"] = vsan_vm_network_vlan_id
    new_vcf_json_py["networkSpecs"][1]["mtu"] = vsan_vm_network_mtu
    new_vcf_json_py["networkSpecs"][1]["networkType"] = "VSAN"
    new_vcf_json_py["networkSpecs"][1]["gateway"] = vsan_vm_network_gateway
    new_vcf_json_py["networkSpecs"].append({})
    new_vcf_json_py["networkSpecs"][2]["subnet"] = vmotion_vm_network_subnet
    new_vcf_json_py["networkSpecs"][2]["includeIpAddressRanges"] = []
    new_vcf_json_py["networkSpecs"][2]["includeIpAddressRanges"].append({})
    new_vcf_json_py["networkSpecs"][2]["includeIpAddressRanges"][0]["startIpAddress"] = vmotion_pool_start_ip
    new_vcf_json_py["networkSpecs"][2]["includeIpAddressRanges"][0]["endIpAddress"] = vmotion_pool_end_ip
    new_vcf_json_py["networkSpecs"][2]["vlanId"] = vmotion_vm_network_vlan_id
    new_vcf_json_py["networkSpecs"][2]["mtu"] = vmotion_vm_network_mtu
    new_vcf_json_py["networkSpecs"][2]["networkType"] = "VMOTION"
    new_vcf_json_py["networkSpecs"][2]["gateway"] = vmotion_vm_network_gateway
    new_vcf_json_py["nsxtSpec"] = {}
    new_vcf_json_py["nsxtSpec"]["nsxtManagerSize"] = nsxt_manager_size
    new_vcf_json_py["nsxtSpec"]["nsxtManagers"] = []
    new_vcf_json_py["nsxtSpec"]["nsxtManagers"].append({})
    new_vcf_json_py["nsxtSpec"]["nsxtManagers"][0]["hostname"] = nsx_mgr_a_hostname
    new_vcf_json_py["nsxtSpec"]["nsxtManagers"][0]["ip"] = nsx_mgr_a_ip
    new_vcf_json_py["nsxtSpec"]["nsxtManagers"].append({})
    new_vcf_json_py["nsxtSpec"]["nsxtManagers"][1]["hostname"] = nsx_mgr_b_hostname
    new_vcf_json_py["nsxtSpec"]["nsxtManagers"][1]["ip"] = nsx_mgr_b_ip
    new_vcf_json_py["nsxtSpec"]["nsxtManagers"].append({})
    new_vcf_json_py["nsxtSpec"]["nsxtManagers"][2]["hostname"] = nsx_mgr_c_hostname
    new_vcf_json_py["nsxtSpec"]["nsxtManagers"][2]["ip"] = nsx_mgr_c_ip
    new_vcf_json_py["nsxtSpec"]["rootNsxtManagerPassword"] = nsxm_root_password
    new_vcf_json_py["nsxtSpec"]["nsxtAdminPassword"] = nsxm_admin_password
    new_vcf_json_py["nsxtSpec"]["nsxtAuditPassword"] = nsxm_audit_password
    new_vcf_json_py["nsxtSpec"]["overLayTransportZone"] = {}
    new_vcf_json_py["nsxtSpec"]["overLayTransportZone"]["zoneName"] = ""
    new_vcf_json_py["nsxtSpec"]["overLayTransportZone"]["networkName"] = ""
    new_vcf_json_py["nsxtSpec"]["vlanTransportZone"] = {}
    new_vcf_json_py["nsxtSpec"]["vlanTransportZone"]["zoneName"] = ""
    new_vcf_json_py["nsxtSpec"]["vlanTransportZone"]["networkName"] = ""
    new_vcf_json_py["nsxtSpec"]["vip"] = nsx_mgr_vip
    new_vcf_json_py["nsxtSpec"]["vipFqdn"] = nsx_mgr_hostname
    new_vcf_json_py["nsxtSpec"]["nsxtLicense"] = nsx_license_key
    new_vcf_json_py["nsxtSpec"]["transportVlanId"] = nsx_host_overlay_vlan_id
    new_vcf_json_py["nsxtSpec"]["ipAddressPoolSpec"] = {}
    new_vcf_json_py["nsxtSpec"]["ipAddressPoolSpec"]["name"] = "sfo01-m01-cl01-tep01" #default - doesnt exist anywhere in the workbook
    new_vcf_json_py["nsxtSpec"]["ipAddressPoolSpec"]["description"] = "ESXi Host Overlay TEP IP Pool" #default - doesnt exist anywhere in the workbook
    new_vcf_json_py["nsxtSpec"]["ipAddressPoolSpec"]["subnets"] = []
    new_vcf_json_py["nsxtSpec"]["ipAddressPoolSpec"]["subnets"].append({})
    new_vcf_json_py["nsxtSpec"]["ipAddressPoolSpec"]["subnets"][0]["ipAddressPoolRanges"] = []
    new_vcf_json_py["nsxtSpec"]["ipAddressPoolSpec"]["subnets"][0]["ipAddressPoolRanges"].append({})
    new_vcf_json_py["nsxtSpec"]["ipAddressPoolSpec"]["subnets"][0]["ipAddressPoolRanges"][0]["start"] = host_tep_overlay_pool_start_ip
    new_vcf_json_py["nsxtSpec"]["ipAddressPoolSpec"]["subnets"][0]["ipAddressPoolRanges"][0]["end"] = host_tep_overlay_pool_end_ip
    new_vcf_json_py["nsxtSpec"]["ipAddressPoolSpec"]["subnets"][0]["cidr"] = nsx_host_overlay_subnet
    new_vcf_json_py["nsxtSpec"]["ipAddressPoolSpec"]["subnets"][0]["gateway"] = nsx_host_overlay_gateway
    new_vcf_json_py["vsanSpec"] = {}
    new_vcf_json_py["vsanSpec"]["vsanName"] = vsan_datastore_name
    new_vcf_json_py["vsanSpec"]["licenseFile"] = vsan_license_key
    new_vcf_json_py["vsanSpec"]["datastoreName"] = vsan_datastore_name
    new_vcf_json_py["dvsSpecs"] = []
    new_vcf_json_py["dvsSpecs"].append({})
    new_vcf_json_py["dvsSpecs"][0]["mtu"] = 8490 #default - doesnt exist anywhere in the workbook
    new_vcf_json_py["dvsSpecs"][0]["niocSpecs"] = []
    new_vcf_json_py["dvsSpecs"][0]["niocSpecs"].append({})
    #Keep all of the niocspecs defaults - these are vmware standards
    new_vcf_json_py["dvsSpecs"][0]["niocSpecs"][0]["trafficType"] = "VSAN"
    new_vcf_json_py["dvsSpecs"][0]["niocSpecs"][0]["value"] = "HIGH"
    new_vcf_json_py["dvsSpecs"][0]["niocSpecs"].append({})
    new_vcf_json_py["dvsSpecs"][0]["niocSpecs"][1]["trafficType"] = "VMOTION"
    new_vcf_json_py["dvsSpecs"][0]["niocSpecs"][1]["value"] = "LOW"
    new_vcf_json_py["dvsSpecs"][0]["niocSpecs"].append({})
    new_vcf_json_py["dvsSpecs"][0]["niocSpecs"][2]["trafficType"] = "VDP"
    new_vcf_json_py["dvsSpecs"][0]["niocSpecs"][2]["value"] = "LOW"
    new_vcf_json_py["dvsSpecs"][0]["niocSpecs"].append({})
    new_vcf_json_py["dvsSpecs"][0]["niocSpecs"][3]["trafficType"] = "VIRTUALMACHINE"
    new_vcf_json_py["dvsSpecs"][0]["niocSpecs"][3]["value"] = "HIGH"
    new_vcf_json_py["dvsSpecs"][0]["niocSpecs"].append({})
    new_vcf_json_py["dvsSpecs"][0]["niocSpecs"][4]["trafficType"] = "MANAGEMENT"
    new_vcf_json_py["dvsSpecs"][0]["niocSpecs"][4]["value"] = "NORMAL"
    new_vcf_json_py["dvsSpecs"][0]["niocSpecs"].append({})
    new_vcf_json_py["dvsSpecs"][0]["niocSpecs"][5]["trafficType"] = "NFS"
    new_vcf_json_py["dvsSpecs"][0]["niocSpecs"][5]["value"] = "LOW"
    new_vcf_json_py["dvsSpecs"][0]["niocSpecs"].append({})
    new_vcf_json_py["dvsSpecs"][0]["niocSpecs"][6]["trafficType"] = "HBR"
    new_vcf_json_py["dvsSpecs"][0]["niocSpecs"][6]["value"] = "LOW"
    new_vcf_json_py["dvsSpecs"][0]["niocSpecs"].append({})
    new_vcf_json_py["dvsSpecs"][0]["niocSpecs"][7]["trafficType"] = "FAULTTOLERANCE"
    new_vcf_json_py["dvsSpecs"][0]["niocSpecs"][7]["value"] = "LOW"
    new_vcf_json_py["dvsSpecs"][0]["niocSpecs"].append({})
    new_vcf_json_py["dvsSpecs"][0]["niocSpecs"][8]["trafficType"] = "ISCSI"
    new_vcf_json_py["dvsSpecs"][0]["niocSpecs"][8]["value"] = "LOW"
    #End default niocspecs
    new_vcf_json_py["dvsSpecs"][0]["dvsName"] = vds_name
    new_vcf_json_py["dvsSpecs"][0]["vmnics"] = vds_pnics
    #Keep network defaults - these are vmware standards
    new_vcf_json_py["dvsSpecs"][0]["networks"] = ["MANAGEMENT", "VSAN", "VMOTION"]
    #End network defaults
    new_vcf_json_py["clusterSpec"] = {}
    new_vcf_json_py["clusterSpec"]["clusterName"] = mgt_cluster_name
    new_vcf_json_py["clusterSpec"]["clusterEvcMode"] = mgt_cluster_evc_settings
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"] = []
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"].append({})
    #Defaults - values below don't exist in the workbook, these can be changed later via vCenter
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][0]["cpuSharesLevel"] = "high"
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][0]["cpuSharesValue"] = 0
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][0]["name"] = "sddc-mgmt"
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][0]["memorySharesValue"] = 0
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][0]["cpuReservationPercentage"] = 0
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][0]["memoryLimit"] = -1
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][0]["memoryReservationPercentage"] = 0
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][0]["cpuReservationExpandable"] = True
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][0]["memoryReservationExpandable"] = True 
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][0]["memorySharesLevel"] = "normal"
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][0]["cpuLimit"] = -1
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][0]["type"] = "management"
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"].append({})
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][1]["cpuSharesLevel"] = "high"
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][1]["cpuSharesValue"] = 0
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][1]["name"] = "sddc-network"
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][1]["memorySharesValue"] = 0
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][1]["cpuReservationPercentage"] = 0
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][1]["memoryLimit"] = -1
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][1]["memoryReservationPercentage"] = 0
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][1]["cpuReservationExpandable"] = True
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][1]["memoryReservationExpandable"] = True 
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][1]["memorySharesLevel"] = "normal"
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][1]["cpuLimit"] = -1
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][1]["type"] = "network"
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"].append({})
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][2]["cpuSharesLevel"] = "normal"
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][2]["cpuSharesValue"] = 0
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][2]["name"] = "sddc-compute"
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][2]["memorySharesValue"] = 0
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][2]["cpuReservationPercentage"] = 0
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][2]["memoryLimit"] = -1
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][2]["memoryReservationPercentage"] = 0
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][2]["cpuReservationExpandable"] = True
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][2]["memoryReservationExpandable"] = True 
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][2]["memorySharesLevel"] = "normal"
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][2]["cpuLimit"] = -1
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][2]["type"] = "compute"
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"].append({})
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][3]["name"] = "user-compute"
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][3]["type"] = "compute"
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][3]["cpuReservationMhz"] = 2100
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][3]["cpuLimit"] = -1
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][3]["cpuReservationExpandable"] = True 
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][3]["cpuSharesLevel"] = "normal"
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][3]["memoryReservationMb"] = 3128
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][3]["memoryReservationExpandable"] = True 
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][3]["memorySharesLevel"] = "normal"
    new_vcf_json_py["clusterSpec"]["resourcePoolSpecs"][3]["memorySharesValue"] = 0
    new_vcf_json_py["pscSpecs"] = []
    new_vcf_json_py["pscSpecs"].append({})
    new_vcf_json_py["pscSpecs"][0]["pscId"] = "psc-1" #default - no value in workbook
    new_vcf_json_py["pscSpecs"][0]["pscSsoSpec"] = {}
    new_vcf_json_py["pscSpecs"][0]["pscSsoSpec"]["ssoDomain"] = "vsphere.local" #default - no value in workbook
    new_vcf_json_py["pscSpecs"][0]["adminUserSsoPassword"] = vc_admin_password
    new_vcf_json_py["vcenterSpec"] = {}
    new_vcf_json_py["vcenterSpec"]["vcenterIp"] = vcsa_ip
    new_vcf_json_py["vcenterSpec"]["vcenterHostname"] = vcsa_hostname
    new_vcf_json_py["vcenterSpec"]["licenseFile"] = vcenter_license_key
    new_vcf_json_py["vcenterSpec"]["rootVcenterPassword"] = vc_root_password
    new_vcf_json_py["vcenterSpec"]["vmSize"] = vcsa_size

    esxi_values_from_xls_length = len(esxi_values_from_xls)
    i=0
    new_vcf_json_py["hostSpecs"] = []
    while i < esxi_values_from_xls_length:
        if esxi_values_from_xls[i]["hostname"]:
            new_vcf_json_py["hostSpecs"].append({})
            new_vcf_json_py["hostSpecs"][i]["credentials"] = {}
            new_vcf_json_py["hostSpecs"][i]["username"] = "root" #hardcoded
            new_vcf_json_py["hostSpecs"][i]["password"] = esxi_password
            new_vcf_json_py["hostSpecs"][i]["ipAddressPrivate"] = {}
            esxi_cidr = management_vm_network_subnet[-2:]
            esxi_netmask = get_netmask(esxi_cidr)
            new_vcf_json_py["hostSpecs"][i]["ipAddressPrivate"]["subnet"] = esxi_netmask
            new_vcf_json_py["hostSpecs"][i]["ipAddressPrivate"]["cidr"] = esxi_cidr
            new_vcf_json_py["hostSpecs"][i]["ipAddressPrivate"]["ipAddress"] = esxi_values_from_xls[i]["ip"]
            new_vcf_json_py["hostSpecs"][i]["ipAddressPrivate"]["gateway"] = management_vm_network_gateway
            new_vcf_json_py["hostSpecs"][i]["hostname"] = esxi_values_from_xls[i]["hostname"]
            new_vcf_json_py["hostSpecs"][i]["vSwitch"] = "vSwitch0" #hardcoded
            new_vcf_json_py["hostSpecs"][i]["serverId"] = "host-"+str(i) #hardcoded
            new_vcf_json_py["hostSpecs"][i]["association"] = datacenter_name
        i=i+1
    return new_vcf_json_py