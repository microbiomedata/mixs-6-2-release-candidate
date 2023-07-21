# Slot: drug_usage


_Any drug used by subject and the frequency of usage; can include multiple drugs used_



URI: [MIXS:0000894](https://w3id.org/mixs/0000894)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HumanAssociated](HumanAssociated.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| Lipitor;2/day |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | drug name;frequency |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: drug_usage
annotations:
  Expected_value:
    tag: Expected_value
    value: drug name;frequency
description: Any drug used by subject and the frequency of usage; can include multiple
  drugs used
title: drug usage
notes:
- drug
- use
examples:
- value: Lipitor;2/day
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text};{integer}/[year|month|week|day|hour]'
slot_uri: MIXS:0000894
multivalued: true
alias: drug_usage
domain_of:
- HumanAssociated
range: string
required: false
recommended: false

```
</details>