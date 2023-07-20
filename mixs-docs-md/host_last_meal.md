# Slot: host_last_meal


_Content of last meal and time since feeding; can include multiple values_



URI: [MIXS:0000870](https://w3id.org/mixs/0000870)



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

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: host_last_meal
description: Content of last meal and time since feeding; can include multiple values
title: host last meal
notes:
- host
- host.
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text};{duration}'
slot_uri: MIXS:0000870
multivalued: true
alias: host_last_meal
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

```
</details>