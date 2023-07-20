# Slot: gaseous_environment


_Use of conditions with differing gaseous environments; should include the name of gaseous compound, amount administered, treatment duration, interval and total experimental duration; can include multiple gaseous environment regimens_



URI: [MIXS:0000558](https://w3id.org/mixs/0000558)



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
| nitric oxide;0.5 micromole per liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | micromole per liter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: gaseous_environment
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: micromole per liter
description: Use of conditions with differing gaseous environments; should include
  the name of gaseous compound, amount administered, treatment duration, interval
  and total experimental duration; can include multiple gaseous environment regimens
title: gaseous environment
notes:
- environment
examples:
- value: nitric oxide;0.5 micromole per liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000558
multivalued: true
alias: gaseous_environment
domain_of:
- Agriculture
- PlantAssociated
range: string

```
</details>