# Slot: association_duration


_Time spent in host of the symbiotic organism at the time of sampling; relevant scale depends on symbiotic organism and study_



URI: [MIXS:0001299](https://w3id.org/mixs/0001299)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[SymbiontAssociated](SymbiontAssociated.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | year, day, hour |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: association_duration
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: year, day, hour
description: Time spent in host of the symbiotic organism at the time of sampling;
  relevant scale depends on symbiotic organism and study
title: duration of association with the host
notes:
- duration
- host
- host.
- period
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0001299
multivalued: false
alias: association_duration
domain_of:
- SymbiontAssociated
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>