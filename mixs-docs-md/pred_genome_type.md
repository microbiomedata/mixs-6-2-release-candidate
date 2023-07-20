# Slot: pred_genome_type


_Type of genome predicted for the UViG_



URI: [MIXS:0000082](https://w3id.org/mixs/0000082)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Miuvig](Miuvig.md) |  |  yes  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| dsDNA |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | enumeration |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: pred_genome_type
annotations:
  Expected_value:
    tag: Expected_value
    value: enumeration
description: Type of genome predicted for the UViG
title: predicted genome type
notes:
- predict
- type
examples:
- value: dsDNA
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '[DNA|dsDNA|ssDNA|RNA|dsRNA|ssRNA|ssRNA (+)|ssRNA (-)|mixed|uncharacterized]'
slot_uri: MIXS:0000082
multivalued: false
alias: pred_genome_type
domain_of:
- Miuvig
range: string

```
</details>