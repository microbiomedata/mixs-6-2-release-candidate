# Slot: tan


_Total Acid Number(TAN) is a measurement of acidity that is determined by the amount ofpotassium hydroxidein milligrams that is needed to neutralize the acids in one gram of oil.It is an important quality measurement ofcrude oil. (source: https://en.wikipedia.org/wiki/Total_acid_number)_



URI: [MIXS:0000120](https://w3id.org/mixs/0000120)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HydrocarbonResourcesCores](HydrocarbonResourcesCores.md) |  |  no  |
[HydrocarbonResourcesFluidsSwabs](HydrocarbonResourcesFluidsSwabs.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Recommended: True

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | milligram per liter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: tan
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: milligram per liter
description: 'Total Acid Number(TAN) is a measurement of acidity that is determined
  by the amount ofpotassium hydroxidein milligrams that is needed to neutralize the
  acids in one gram of oil.It is an important quality measurement ofcrude oil. (source:
  https://en.wikipedia.org/wiki/Total_acid_number)'
title: total acid number
notes:
- number
- total
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000120
multivalued: false
alias: tan
domain_of:
- HydrocarbonResourcesCores
- HydrocarbonResourcesFluidsSwabs
range: string
recommended: true
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>