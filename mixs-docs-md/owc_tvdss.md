# Slot: owc_tvdss


_Depth of the original oil water contact (OWC) zone (average) (m TVDSS)_



URI: [MIXS:0000405](https://w3id.org/mixs/0000405)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HydrocarbonResourcesCores](HydrocarbonResourcesCores.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | meter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: owc_tvdss
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: meter
description: Depth of the original oil water contact (OWC) zone (average) (m TVDSS)
title: oil water contact depth
notes:
- depth
- oil
- water
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000405
multivalued: false
alias: owc_tvdss
domain_of:
- HydrocarbonResourcesCores
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>