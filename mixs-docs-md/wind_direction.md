# Slot: wind_direction


_Wind direction is the direction from which a wind originates_



URI: [MIXS:0000757](https://w3id.org/mixs/0000757)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Air](Air.md) |  |  yes  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | degrees or cardinal direction |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: wind_direction
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: degrees or cardinal direction
description: Wind direction is the direction from which a wind originates
title: wind direction
notes:
- direction
- wind
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000757
multivalued: false
alias: wind_direction
domain_of:
- Air
- FoodFarmEnvironment
range: string
required: false
recommended: false

```
</details>