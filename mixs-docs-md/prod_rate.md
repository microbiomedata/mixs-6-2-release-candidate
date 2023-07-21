# Slot: prod_rate


_Oil and/or gas production rates per well (e.g. 524 m3 / day)_



URI: [MIXS:0000452](https://w3id.org/mixs/0000452)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HydrocarbonResourcesFluidsSwabs](HydrocarbonResourcesFluidsSwabs.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Recommended: True

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | cubic meter per day |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: prod_rate
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: cubic meter per day
description: Oil and/or gas production rates per well (e.g. 524 m3 / day)
title: production rate
notes:
- production
- rate
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000452
multivalued: false
alias: prod_rate
domain_of:
- HydrocarbonResourcesFluidsSwabs
range: string
recommended: true
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>