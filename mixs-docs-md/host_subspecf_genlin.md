# Slot: host_subspecf_genlin


_Information about the genetic distinctness of the host organism below the subspecies level e.g., serovar, serotype, biotype, ecotype, variety, cultivar, or any relevant genetic typing schemes like Group I plasmid. Subspecies should not be recorded in this term, but in the NCBI taxonomy. Supply both the lineage name and the lineage rank separated by a colon, e.g., biovar:abc123_



URI: [MIXS:0001318](https://w3id.org/mixs/0001318)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  no  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  no  |
[HostAssociated](HostAssociated.md) |  |  no  |
[PlantAssociated](PlantAssociated.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| serovar:Newport, variety:glabrum, cultivar: Red Delicious |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | Genetic lineage below lowest rank of NCBI taxonomy, which is subspecies, e.g. serovar, biotype, ecotype, variety, cultivar |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: host_subspecf_genlin
annotations:
  Expected_value:
    tag: Expected_value
    value: Genetic lineage below lowest rank of NCBI taxonomy, which is subspecies,
      e.g. serovar, biotype, ecotype, variety, cultivar
description: Information about the genetic distinctness of the host organism below
  the subspecies level e.g., serovar, serotype, biotype, ecotype, variety, cultivar,
  or any relevant genetic typing schemes like Group I plasmid. Subspecies should not
  be recorded in this term, but in the NCBI taxonomy. Supply both the lineage name
  and the lineage rank separated by a colon, e.g., biovar:abc123
title: host subspecific genetic lineage
notes:
- host
- host.
- lineage
examples:
- value: 'serovar:Newport, variety:glabrum, cultivar: Red Delicious'
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{rank name}:{text}'
slot_uri: MIXS:0001318
multivalued: true
alias: host_subspecf_genlin
domain_of:
- Agriculture
- FoodFarmEnvironment
- HostAssociated
- PlantAssociated
range: string
required: false
recommended: false

```
</details>