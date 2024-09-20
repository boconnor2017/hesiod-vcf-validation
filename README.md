# Hesiod VCF Validation
Uses [Project Hesiod](https://github.com/boconnor2017/hesiod), a Photon based approach to validate your VCF configurations. There are two goals with this project:

| Goal | Description |
|------|-------------|
| Provide an alternative to the VCF Prerequisites Spreadsheet | The solutions in this repository center around the lesser known VCF JSON file. Using the JSON file you can build your own CLI or UI to populate the JSON file. This opens the door for better scale, automation, and self service. |
| Provide tools to document the VCF configuration | The solutions in this repository provide open source approaches to scraping the VCF JSON and producing Markdown files. These Markdown files can be imported into Confluence or exported to PDF using Visual Studio extensions. |

# Prerequisites
The following binaries are **required** to run hesiod-vcf-validation:

| Requirement | Description |
|-------------|-------------|
| PhotonOS OVA | version 5.0 recommended (download from [VMware GitHub](https://vmware.github.io/photon/)) |

# Quick Start
Deploy Photon OS OVA to the physical server. Follow the steps in the [Hesiod Photon OS Quick Start](https://github.com/boconnor2017/hesiod/blob/main/photon/readme.md) readme file to prep the Photon server for VCF. 

*Recommended: run these scripts as root.*
```
cd /usr/local/
```
```
git clone https://github.com/boconnor2017/hesiod-vcf-validation
```
```
cp -r hesiod/python/ hesiod-vcf5/hesiod
```
```
cd hesiod-vcf-validation
```