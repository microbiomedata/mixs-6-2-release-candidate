# Slot: herbicide_regm


_Information about treatment involving use of herbicides; information about treatment involving use of growth hormones; should include the name of herbicide, amount administered, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple regimens_



URI: [MIXS:0000561](https://w3id.org/mixs/0000561)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[PlantAssociated](PlantAssociated.md) |  |  yes  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| atrazine;10 milligram per liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | gram, mole per liter, milligram per liter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: herbicide_regm
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: gram, mole per liter, milligram per liter
description: Information about treatment involving use of herbicides; information
  about treatment involving use of growth hormones; should include the name of herbicide,
  amount administered, treatment regimen including how many times the treatment was
  repeated, how long each treatment lasted, and the start and end time of the entire
  treatment; can include multiple regimens
title: herbicide regimen
notes:
- regimen
examples:
- value: atrazine;10 milligram per liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000561
multivalued: true
alias: herbicide_regm
domain_of:
- Agriculture
- PlantAssociated
range: string

```
</details>