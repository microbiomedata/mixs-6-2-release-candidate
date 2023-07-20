# Slot: ethnicity


_A category of people who identify with each other, usually on the basis of presumed similarities such as a common language, ancestry, history, society, culture, nation or social treatment within their residing area. https://en.wikipedia.org/wiki/List_of_contemporary_ethnic_groups_



URI: [MIXS:0000895](https://w3id.org/mixs/0000895)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HumanAssociated](HumanAssociated.md) |  |  no  |
[HumanGut](HumanGut.md) |  |  no  |
[HumanOral](HumanOral.md) |  |  no  |
[HumanSkin](HumanSkin.md) |  |  no  |
[HumanVaginal](HumanVaginal.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| native american |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | text recommend from Wikipedia list |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: ethnicity
annotations:
  Expected_value:
    tag: Expected_value
    value: text recommend from Wikipedia list
description: A category of people who identify with each other, usually on the basis
  of presumed similarities such as a common language, ancestry, history, society,
  culture, nation or social treatment within their residing area. https://en.wikipedia.org/wiki/List_of_contemporary_ethnic_groups
title: ethnicity
examples:
- value: native american
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text}'
slot_uri: MIXS:0000895
multivalued: true
alias: ethnicity
domain_of:
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