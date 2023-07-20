# Slot: microb_start_count


_Total cell count of starter culture per gram, volume or area of sample and the method that was used for the enumeration (e.g. qPCR, atp, mpn, etc.) should also be provided. (example : total prokaryotes; 3.5e7 cells per ml; qPCR)_



URI: [MIXS:0001218](https://w3id.org/mixs/0001218)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodHumanFoods](FoodHumanFoods.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| total prokaryotes;3.5e9 colony forming units per milliliter;spread plate |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | organism name; measurement value; enumeration || Preferred_unit | colony forming units per milliliter; colony forming units per gram of dry weight |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: microb_start_count
annotations:
  Expected_value:
    tag: Expected_value
    value: organism name; measurement value; enumeration
  Preferred_unit:
    tag: Preferred_unit
    value: colony forming units per milliliter; colony forming units per gram of dry
      weight
description: 'Total cell count of starter culture per gram, volume or area of sample
  and the method that was used for the enumeration (e.g. qPCR, atp, mpn, etc.) should
  also be provided. (example : total prokaryotes; 3.5e7 cells per ml; qPCR)'
title: microbial starter organism count
notes:
- count
- microbial
- organism
examples:
- value: total prokaryotes;3.5e9 colony forming units per milliliter;spread plate
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text};{float} {unit};[ATP|MPN|qPCR|spread plate|other]'
slot_uri: MIXS:0001218
multivalued: false
alias: microb_start_count
domain_of:
- FoodHumanFoods
range: string
required: false
recommended: false

```
</details>