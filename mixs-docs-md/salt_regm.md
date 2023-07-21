# Slot: salt_regm


_Information about treatment involving use of salts as supplement to liquid and soil growth media; should include the name of salt, amount administered, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple salt regimens_



URI: [MIXS:0000582](https://w3id.org/mixs/0000582)



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
| NaCl;5 gram per liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | gram, microgram, mole per liter, gram per liter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: salt_regm
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: gram, microgram, mole per liter, gram per liter
description: Information about treatment involving use of salts as supplement to liquid
  and soil growth media; should include the name of salt, amount administered, treatment
  regimen including how many times the treatment was repeated, how long each treatment
  lasted, and the start and end time of the entire treatment; can include multiple
  salt regimens
title: salt regimen
notes:
- regimen
- salt
examples:
- value: NaCl;5 gram per liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000582
multivalued: true
alias: salt_regm
domain_of:
- Agriculture
- PlantAssociated
range: string

```
</details>