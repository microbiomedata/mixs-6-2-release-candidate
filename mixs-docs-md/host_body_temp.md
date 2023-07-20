# Slot: host_body_temp


_Core body temperature of the host when sample was collected_



URI: [MIXS:0000274](https://w3id.org/mixs/0000274)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HostAssociated](HostAssociated.md) |  |  yes  |
[HumanAssociated](HumanAssociated.md) |  |  yes  |
[HumanGut](HumanGut.md) |  |  yes  |
[HumanOral](HumanOral.md) |  |  yes  |
[HumanSkin](HumanSkin.md) |  |  yes  |
[HumanVaginal](HumanVaginal.md) |  |  yes  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | degree Celsius |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: host_body_temp
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: degree Celsius
description: Core body temperature of the host when sample was collected
title: host body temperature
notes:
- body
- host
- host.
- temperature
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000274
multivalued: false
alias: host_body_temp
domain_of:
- HostAssociated
- HumanAssociated
- HumanGut
- HumanOral
- HumanSkin
- HumanVaginal
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>