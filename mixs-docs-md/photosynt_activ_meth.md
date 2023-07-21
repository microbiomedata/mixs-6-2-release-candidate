# Slot: photosynt_activ_meth


_Reference or method used in measurement of photosythetic activity_



URI: [MIXS:0001336](https://w3id.org/mixs/0001336)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True

* Recommended: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: photosynt_activ_meth
description: Reference or method used in measurement of photosythetic activity
title: photosynthetic activity method
notes:
- method
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0001336
multivalued: true
alias: photosynt_activ_meth
domain_of:
- Agriculture
range: string
recommended: true
structured_pattern:
  syntax: '{PMID}|{DOI}|{URL}|{text}'
  interpolated: true
  partial_match: true

```
</details>