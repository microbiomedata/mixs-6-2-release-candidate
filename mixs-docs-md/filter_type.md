# Slot: filter_type


_A device which removes solid particulates or airborne molecular contaminants_



URI: [MIXS:0000765](https://w3id.org/mixs/0000765)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [FILTERTYPEENUM](FILTERTYPEENUM.md)

* Multivalued: True

* Required: True






## Examples

| Value |
| --- |
| HEPA |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: filter_type
description: A device which removes solid particulates or airborne molecular contaminants
title: filter type
notes:
- filter
- type
examples:
- value: HEPA
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000765
multivalued: true
alias: filter_type
domain_of:
- BuiltEnvironment
range: FILTER_TYPE_ENUM
required: true

```
</details>