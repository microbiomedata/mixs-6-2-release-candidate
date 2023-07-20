# Slot: host_hiv_stat


_HIV status of subject, if yes HAART initiation status should also be indicated as [YES or NO]_



URI: [MIXS:0000265](https://w3id.org/mixs/0000265)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HumanAssociated](HumanAssociated.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| yes;yes |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | HIV status;HAART initiation status |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: host_hiv_stat
annotations:
  Expected_value:
    tag: Expected_value
    value: HIV status;HAART initiation status
description: HIV status of subject, if yes HAART initiation status should also be
  indicated as [YES or NO]
title: host HIV status
notes:
- host
- host.
- status
examples:
- value: yes;yes
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{boolean};{boolean}'
slot_uri: MIXS:0000265
multivalued: false
alias: host_hiv_stat
domain_of:
- HumanAssociated
range: string
required: false
recommended: false

```
</details>