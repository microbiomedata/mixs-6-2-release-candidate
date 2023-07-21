# Slot: sieving


_Collection design of pooled samples and/or sieve size and amount of sample sieved_



URI: [MIXS:0000322](https://w3id.org/mixs/0000322)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[Soil](Soil.md) |  |  yes  |
[MimsSoil](MimsSoil.md) |  |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | design name and/or size;amount |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: sieving
annotations:
  Expected_value:
    tag: Expected_value
    value: design name and/or size;amount
description: Collection design of pooled samples and/or sieve size and amount of sample
  sieved
title: composite design/sieving
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000322
multivalued: false
alias: sieving
domain_of:
- Agriculture
- Soil
range: string

```
</details>