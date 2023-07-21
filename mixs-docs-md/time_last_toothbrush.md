# Slot: time_last_toothbrush


_Specification of the time since last toothbrushing_



URI: [MIXS:0000924](https://w3id.org/mixs/0000924)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HumanOral](HumanOral.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^P(?!$)(\d+Y)?(\d+M)?(\d+W)?(\d+D)?(T(?=\d+[HMS])(\d+H)?(\d+M)?(\d+S)?)?$`






## Examples

| Value |
| --- |
| PT2H45M |

## Comments

* P2H45M does not match ^P(?!$)(\\d+Y)?(\\d+M)?(\\d+W)?(\\d+D)?(T(?=\\d+[HMS])(\\d+H)?(\\d+M)?(\\d+S)?)?$
* problematic ISO 8601 period validation

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: time_last_toothbrush
description: Specification of the time since last toothbrushing
title: time since last toothbrushing
notes:
- time
comments:
- P2H45M does not match ^P(?!$)(\\d+Y)?(\\d+M)?(\\d+W)?(\\d+D)?(T(?=\\d+[HMS])(\\d+H)?(\\d+M)?(\\d+S)?)?$
- problematic ISO 8601 period validation
examples:
- value: PT2H45M
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000924
alias: time_last_toothbrush
domain_of:
- HumanOral
range: string
required: false
recommended: false
pattern: ^P(?!$)(\d+Y)?(\d+M)?(\d+W)?(\d+D)?(T(?=\d+[HMS])(\d+H)?(\d+M)?(\d+S)?)?$

```
</details>