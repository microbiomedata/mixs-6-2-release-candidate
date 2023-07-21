# Slot: window_status


_Defines whether the windows were open or closed during environmental testing_



URI: [MIXS:0000855](https://w3id.org/mixs/0000855)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [WINDOWSTATUSENUM](WINDOWSTATUSENUM.md)






## Examples

| Value |
| --- |
| open |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: window_status
description: Defines whether the windows were open or closed during environmental
  testing
title: window status
notes:
- status
- window
examples:
- value: open
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000855
multivalued: false
alias: window_status
domain_of:
- BuiltEnvironment
range: WINDOW_STATUS_ENUM
required: false
recommended: false

```
</details>