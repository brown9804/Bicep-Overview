# Isolated network module

## Purpose and architecture

Deploy a VNet with one workload subnet and an attached NSG.
A priority-4096 rule denies **all inbound** traffic, including VNet traffic,
unless a later approved higher-priority allow rule is introduced.
The NSG reference creates an implicit deployment dependency.

This is not a complete egress isolation design: default outbound rules remain.
No NAT, firewall, VPN, DNS, public IP, compute, or private endpoint is included.

## Prerequisites and inputs

Offline compilation requires Azure CLI/Bicep only. Live deployment requires an
approved resource group, networking permissions, compatible policies/region,
and reviewed non-overlapping address ranges.

| Input | Purpose |
| --- | --- |
| `virtualNetworkName` | Required VNet name |
| `location` | Defaults to the target group region |
| `addressPrefix` | VNet CIDR, sample `10.40.0.0/16` |
| `subnetPrefix` | Contained subnet CIDR, sample `10.40.1.0/24` |
| `tags` | Non-sensitive resource metadata |

CIDR containment and overlap are not checked by the Bicep string types.
Output is the VNet management-plane ID.
Read [main.bicep](https://github.com/brown9804/Bicep-Overview/blob/main/modules/isolated-network/main.bicep) and the
[foundation caller](https://github.com/brown9804/Bicep-Overview/blob/main/examples/03-modular-foundation/README.md).

## Validation and optional live deployment

From the repository root:

```shell
az bicep build --file modules/isolated-network/main.bicep --stdout
```

Expected: one VNet, one NSG, and an embedded subnet with NSG association.
For standalone use in an existing dedicated group, Bash:

```bash
az deployment group validate --resource-group "$RESOURCE_GROUP" \
  --template-file modules/isolated-network/main.bicep --parameters virtualNetworkName=learn-vnet
az deployment group what-if --resource-group "$RESOURCE_GROUP" \
  --template-file modules/isolated-network/main.bicep --parameters virtualNetworkName=learn-vnet
az deployment group create --name bicep-overview-network --resource-group "$RESOURCE_GROUP" \
  --template-file modules/isolated-network/main.bicep --parameters virtualNetworkName=learn-vnet
```

Review the selected subscription, addresses, and what-if before create.
After successful deployment, inspect subnet association and effective rules
for a future workload. There is no deployed workload to connectivity-test here.

## Cleanup, security, and costs

VNet/NSG objects have no direct compute charges, but added workloads and
networking services may cost money. Denying inbound is not security accreditation.
Plan explicit workload allow rules and egress controls before adding services.

After removing dependent workloads, endpoints, and subnet consumers:

```bash
az network vnet delete --name learn-vnet --resource-group "$RESOURCE_GROUP"
az network nsg delete --name learn-vnet-nsg --resource-group "$RESOURCE_GROUP"
```

Verify deletion. Use names matching your deployed inputs, and never delete
shared networking without approval.
