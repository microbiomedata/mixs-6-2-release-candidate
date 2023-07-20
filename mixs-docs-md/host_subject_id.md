# Slot: host_subject_id


_A unique identifier by which each subject can be referred to, de-identified_



URI: [MIXS:0000861](https://w3id.org/mixs/0000861)



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
[SymbiontAssociated](SymbiontAssociated.md) |  |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: host_subject_id
description: A unique identifier by which each subject can be referred to, de-identified
title: host subject id
notes:
- host
- host.
- identifier
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000861
multivalued: false
alias: host_subject_id
domain_of:
- HostAssociated
- HumanAssociated
- HumanGut
- HumanOral
- HumanSkin
- HumanVaginal
- SymbiontAssociated
range: string
required: false
recommended: false

```
</details>