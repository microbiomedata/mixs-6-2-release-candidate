# Slot: fungicide_regm


_Information about treatment involving use of fungicides; should include the name of fungicide, amount administered, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple fungicide regimens_



URI: [MIXS:0000557](https://w3id.org/mixs/0000557)



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
| bifonazole;1 mole per liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | gram, mole per liter, milligram per liter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: fungicide_regm
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: gram, mole per liter, milligram per liter
description: Information about treatment involving use of fungicides; should include
  the name of fungicide, amount administered, treatment regimen including how many
  times the treatment was repeated, how long each treatment lasted, and the start
  and end time of the entire treatment; can include multiple fungicide regimens
title: fungicide regimen
notes:
- regimen
examples:
- value: bifonazole;1 mole per liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000557
multivalued: true
alias: fungicide_regm
domain_of:
- Agriculture
- PlantAssociated
range: string

```
</details>