# Slot: host_diet


_Type of diet depending on the host, for animals omnivore, herbivore etc., for humans high-fat, meditteranean etc.; can include multiple diet types_



URI: [MIXS:0000869](https://w3id.org/mixs/0000869)



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


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: host_diet
description: Type of diet depending on the host, for animals omnivore, herbivore etc.,
  for humans high-fat, meditteranean etc.; can include multiple diet types
title: host diet
notes:
- diet
- host
- host.
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000869
multivalued: true
alias: host_diet
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