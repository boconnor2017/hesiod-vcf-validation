# VCF 5.2 Configuration Validation
The following values were pulled from the vcf.json file that will be used during VCF Bringup.

## General
| Parameter | Configured Value |
|-----------|------------------|
| dvSwitch Version | 7.0.0 |
| Management Pool Name | bringup-networkpool |
| SDDC ID | hesiod-vcf-api-01 |

## License Keys
| Parameter | Configured Value |
|-----------|------------------|
| ESXi License Key | RH2FJ-LD457-P8ENR-LY2AH-2186G |
| vCenter License Key | 5M2AM-TCLD6-283NA-09C86-3R6Q1 |
| vSAN License Key | Q00A4-LDJ1L-68CNR-015R0-C8M41 |
| NSX License Key | H4006-DNJ84-Y88D1-0CAA0-2H5P4 |

## Credentials
| Parameter | Configured Value |
|-----------|------------------|
| SDDC Manager Local User Password | VMware123!VMware123! |
| SDDC Manager Root User Username | root |
| SDDC Manager Root User Password | VMware123!VMware123! |
| SDDC Manager Second User Username | vcf |
| SDDC Manager Second User Password | VMware123!VMware123! |
| root NSX Manager Password | VMware123!VMware123! |
| NSX Admin Password | VMware123!VMware123! |
| NSX Audit Password | VMware123!VMware123! |
| Platform Services Controller 1 Admin User SSO Password | VMware123!VMware123! |
| vCenter Root Password | VMware123!VMware123! |
| ESXi Host 1 Username | root |
| ESXi Host 1 Password | VMware123! |
| ESXi Host 2 Username | root |
| ESXi Host 2 Password | VMware123! |
| ESXi Host 3 Username | root |
| ESXi Host 3 Password | VMware123! |
| ESXi Host 4 Username | root |
| ESXi Host 4 Password | VMware123! |

## Network Specs
| Network Type | Subnet | VLAN ID | MTU | Gateway |
|--------------|--------|---------|-----|---------|

| Network Type | Include IP Address Range (Start) | Include IP Address Range (End) |
|---|---|---|
| VSAN | 172.16.11.7 | 172.16.11.48
| VSAN | 172.16.11.3 | 172.16.11.6
| VMOTION | 172.16.12.3 | 172.16.11.48

| Network Type | Include IP Address |
|---|---|
| VSAN | 172.16.11.50 |
| VSAN | 172.16.11.49 |

## Domain Specs
| Parameter | Configured Value |
|-----------|------------------|
| NTP Servers |  |
| Subdomain |  |
| Domain |  |
| Name Server |  |
| Secondary Name Server |  |

## DNS Entries
| Parameter | Hostname | IP Address |
|-----------|----------|------------|
| SDDC Manager |  |  |
| NSX Manager A |  |  |
| NSX Manager B |  |  |
| NSX Manager C |  |  |
| NSX Manager VIP |  |  |
| vCenter |  |  |
| ESXi Host 1 |  |  |
| ESXi Host 2 |  |  |
| ESXi Host 3 |  |  |
| ESXi Host 4 |  |  |

## NSXT Specs
| Parameter | Configured Value |
|-----------|------------------|
| NSX Manager Size |  |
| Overlay Transport Zone Name |  |
| Overlay Transport Network Name |  |
| VLAN Transport Zone Name |  |
| VLAN Transport Network Name |  |

## SDDC Manager Specs
| Parameter | Configured Value |
|-----------|------------------|
| Netmask   |  |

## VSAN Specs
| Parameter | Configured Value |
|-----------|------------------|
| vSAN Name |  |
| Datastore Name |  |

## Distributed Virtual Switch Specs
| Parameter | Configured Value |
|-----------|------------------|
| MTU |  |
| VSAN Traffic Type |  |
| VMOTION Traffic Type |  |
| VDP Traffic Type |  |
| VIRTUALMACHINE Traffic Type |  |
| MANAGEMENT Traffic Type |  |
| NFS Traffic Type |  |
| HBR Traffic Type |  |
| FAULTTOLERANCE Traffic Type |  |
| ISCSI Traffic Type |  |
| DVS Name |  |
| vmnics |  |
| Networks |  |

## ESXi Cluster Specs
| Parameter | Configured Value |
|-----------|------------------|
| Cluster Name |  |
| Cluster EVC Mode |  |
| Resource Pool Specs: |  |
| Name |  |
| Type |  |
| CPU Shares Level |  |
| CPU Shares Value |  |
| CPU Limit |  |
| CPU Reservation Percentage |  |
| CPU Reservation Expandable |  |
| Memory Shares Level |  |
| Memory Shares Value |  |
| Memory Limit |  |
| Memery Reservation Percentage |  |
| Memory Reservation Expandable |  |

## Platform Services Controller Specs
| Parameter | Configured Value |
|-----------|------------------|
| PSC ID |  |
| SSO Domain |  |

## vCenter Spec
| Parameter | Configured Value |
|-----------|------------------|
| VM Size |  |

## ESXi Host Specs
| Server ID | Hostname | Association | vSwitch | Subnet Mask | CIDR | Gateway | IP Address |
|-----------|----------|-------------|---------|-------------|------|---------|------------|
|  |  |  |  |  |  |  |  |
