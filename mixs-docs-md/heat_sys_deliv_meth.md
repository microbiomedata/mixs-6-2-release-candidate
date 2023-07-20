# Slot: heat_sys_deliv_meth


_The method by which the heat is delivered through the system_



URI: [MIXS:0000812](https://w3id.org/mixs/0000812)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [HEATSYSDELIVMETHENUM](HEATSYSDELIVMETHENUM.md)






## Examples

| Value |
| --- |
| radiant |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: heat_sys_deliv_meth
description: The method by which the heat is delivered through the system
title: heating system delivery method
notes:
- delivery
- method
examples:
- value: radiant
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000812
multivalued: false
alias: heat_sys_deliv_meth
domain_of:
- BuiltEnvironment
range: HEAT_SYS_DELIV_METH_ENUM
required: false
recommended: false

```
</details>