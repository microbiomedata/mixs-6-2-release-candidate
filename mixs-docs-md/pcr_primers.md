# Slot: pcr_primers


_PCR primers that were used to amplify the sequence of the targeted gene, locus or subfragment. This field should contain all the primers used for a single PCR reaction if multiple forward or reverse primers are present in a single PCR reaction. The primer sequence should be reported in uppercase letters_



URI: [MIXS:0000046](https://w3id.org/mixs/0000046)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[MimarksC](MimarksC.md) |  |  yes  |
[MimarksS](MimarksS.md) |  |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: pcr_primers
description: PCR primers that were used to amplify the sequence of the targeted gene,
  locus or subfragment. This field should contain all the primers used for a single
  PCR reaction if multiple forward or reverse primers are present in a single PCR
  reaction. The primer sequence should be reported in uppercase letters
title: pcr primers
notes:
- pcr
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: FWD:{dna};REV:{dna}
slot_uri: MIXS:0000046
multivalued: false
alias: pcr_primers
domain_of:
- Agriculture
- MimarksC
- MimarksS
range: string

```
</details>