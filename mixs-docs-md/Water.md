# Class: Water



URI: [mixs_6_2_proposal:Water](https://turbomam.github.io/mixs-envo-struct-knowl-extraction/Water)



```mermaid
 classDiagram
    class Water
      EnvironmentalPackage <|-- Water
      
      Water : alkalinity
        
      Water : alkalinity_method
        
      Water : alkyl_diethers
        
      Water : aminopept_act
        
      Water : ammonium
        
      Water : atmospheric_data
        
      Water : bac_prod
        
      Water : bac_resp
        
      Water : bacteria_carb_prod
        
      Water : biomass
        
      Water : bishomohopanol
        
      Water : bromide
        
      Water : calcium
        
      Water : carb_nitro_ratio
        
      Water : chem_administration
        
      Water : chloride
        
      Water : chlorophyll
        
      Water : conduc
        
      Water : density
        
      Water : depth
        
      Water : diether_lipids
        
      Water : diss_carb_dioxide
        
      Water : diss_hydrogen
        
      Water : diss_inorg_carb
        
      Water : diss_inorg_nitro
        
      Water : diss_inorg_phosp
        
      Water : diss_org_carb
        
      Water : diss_org_nitro
        
      Water : diss_oxygen
        
      Water : down_par
        
      Water : elev
        
      Water : fluor
        
      Water : glucosidase_act
        
      Water : light_intensity
        
      Water : magnesium
        
      Water : mean_frict_vel
        
      Water : mean_peak_frict_vel
        
      Water : misc_param
        
      Water : n_alkanes
        
      Water : nitrate
        
      Water : nitrite
        
      Water : nitro
        
      Water : org_carb
        
      Water : org_matter
        
      Water : org_nitro
        
      Water : organism_count
        
      Water : oxy_stat_samp
        
          Water --|> OXY_STAT_SAMP_ENUM : oxy_stat_samp
        
      Water : part_org_carb
        
      Water : part_org_nitro
        
      Water : perturbation
        
      Water : petroleum_hydrocarb
        
      Water : ph
        
      Water : phaeopigments
        
      Water : phosphate
        
      Water : phosplipid_fatt_acid
        
      Water : photon_flux
        
      Water : potassium
        
      Water : pressure
        
      Water : primary_prod
        
      Water : project_name
        
      Water : redox_potential
        
      Water : salinity
        
      Water : samp_name
        
      Water : samp_store_dur
        
      Water : samp_store_loc
        
      Water : samp_store_temp
        
      Water : samp_vol_we_dna_ext
        
      Water : silicate
        
      Water : size_frac_low
        
      Water : size_frac_up
        
      Water : sodium
        
      Water : soluble_react_phosp
        
      Water : sulfate
        
      Water : sulfide
        
      Water : suspend_part_matter
        
      Water : temp
        
      Water : tidal_stage
        
          Water --|> TIDAL_STAGE_ENUM : tidal_stage
        
      Water : tot_depth_water_col
        
      Water : tot_diss_nitro
        
      Water : tot_inorg_nitro
        
      Water : tot_nitro
        
      Water : tot_part_carb
        
      Water : tot_phosp
        
      Water : turbidity
        
      Water : water_current
        
      
```





## Inheritance
* [EnvironmentalPackage](EnvironmentalPackage.md)
    * **Water**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [samp_name](samp_name.md) | 1..1 <br/> [String](String.md) | A local identifier or name that for the material sample used for extracting n... | direct |
| [project_name](project_name.md) | 1..1 <br/> [String](String.md) | Name of the project within which the sequencing was organized | direct |
| [depth](depth.md) | 1..1 <br/> [String](String.md) | The vertical distance below local surface | direct |
| [elev](elev.md) | 0..1 _recommended_ <br/> [String](String.md) | Elevation of the sampling site is its height above a fixed reference point, m... | direct |
| [alkalinity](alkalinity.md) | 0..1 <br/> [String](String.md) | Alkalinity, the ability of a solution to neutralize acids to the equivalence ... | direct |
| [alkalinity_method](alkalinity_method.md) | 0..1 <br/> [String](String.md) | Method used for alkalinity measurement | direct |
| [alkyl_diethers](alkyl_diethers.md) | 0..1 <br/> [String](String.md) | Concentration of alkyl diethers | direct |
| [aminopept_act](aminopept_act.md) | 0..1 <br/> [String](String.md) | Measurement of aminopeptidase activity | direct |
| [ammonium](ammonium.md) | 0..1 <br/> [String](String.md) | Concentration of ammonium in the sample | direct |
| [atmospheric_data](atmospheric_data.md) | 0..* <br/> [String](String.md) | Measurement of atmospheric data; can include multiple data | direct |
| [bacteria_carb_prod](bacteria_carb_prod.md) | 0..1 <br/> [String](String.md) | Measurement of bacterial carbon production | direct |
| [bac_prod](bac_prod.md) | 0..1 <br/> [String](String.md) | Bacterial production in the water column measured by isotope uptake | direct |
| [bac_resp](bac_resp.md) | 0..1 <br/> [String](String.md) | Measurement of bacterial respiration in the water column | direct |
| [biomass](biomass.md) | 0..* <br/> [String](String.md) | Amount of biomass; should include the name for the part of biomass measured, ... | direct |
| [bishomohopanol](bishomohopanol.md) | 0..1 <br/> [String](String.md) | Concentration of bishomohopanol | direct |
| [bromide](bromide.md) | 0..1 <br/> [String](String.md) | Concentration of bromide | direct |
| [calcium](calcium.md) | 0..1 <br/> [String](String.md) | Concentration of calcium in the sample | direct |
| [carb_nitro_ratio](carb_nitro_ratio.md) | 0..1 <br/> [Float](Float.md) | Ratio of amount or concentrations of carbon to nitrogen | direct |
| [chem_administration](chem_administration.md) | 0..* <br/> [String](String.md) | List of chemical compounds administered to the host or site where sampling oc... | direct |
| [chloride](chloride.md) | 0..1 <br/> [String](String.md) | Concentration of chloride in the sample | direct |
| [chlorophyll](chlorophyll.md) | 0..1 <br/> [String](String.md) | Concentration of chlorophyll | direct |
| [conduc](conduc.md) | 0..1 <br/> [String](String.md) | Electrical conductivity of water | direct |
| [density](density.md) | 0..1 <br/> [String](String.md) | Density of the sample, which is its mass per unit volume (aka volumetric mass... | direct |
| [diether_lipids](diether_lipids.md) | 0..* <br/> [String](String.md) | Concentration of diether lipids; can include multiple types of diether lipids | direct |
| [diss_carb_dioxide](diss_carb_dioxide.md) | 0..1 <br/> [String](String.md) | Concentration of dissolved carbon dioxide in the sample or liquid portion of ... | direct |
| [diss_hydrogen](diss_hydrogen.md) | 0..1 <br/> [String](String.md) | Concentration of dissolved hydrogen | direct |
| [diss_inorg_carb](diss_inorg_carb.md) | 0..1 <br/> [String](String.md) | Dissolved inorganic carbon concentration in the sample, typically measured af... | direct |
| [diss_inorg_nitro](diss_inorg_nitro.md) | 0..1 <br/> [String](String.md) | Concentration of dissolved inorganic nitrogen | direct |
| [diss_inorg_phosp](diss_inorg_phosp.md) | 0..1 <br/> [String](String.md) | Concentration of dissolved inorganic phosphorus in the sample | direct |
| [diss_org_carb](diss_org_carb.md) | 0..1 <br/> [String](String.md) | Concentration of dissolved organic carbon in the sample, liquid portion of th... | direct |
| [diss_org_nitro](diss_org_nitro.md) | 0..1 <br/> [String](String.md) | Dissolved organic nitrogen concentration measured as; total dissolved nitroge... | direct |
| [diss_oxygen](diss_oxygen.md) | 0..1 <br/> [String](String.md) | Concentration of dissolved oxygen | direct |
| [down_par](down_par.md) | 0..1 <br/> [String](String.md) | Visible waveband radiance and irradiance measurements in the water column | direct |
| [fluor](fluor.md) | 0..1 <br/> [String](String.md) | Raw or converted fluorescence of water | direct |
| [glucosidase_act](glucosidase_act.md) | 0..1 <br/> [String](String.md) | Measurement of glucosidase activity | direct |
| [light_intensity](light_intensity.md) | 0..1 <br/> [String](String.md) | Measurement of light intensity | direct |
| [magnesium](magnesium.md) | 0..1 <br/> [String](String.md) | Concentration of magnesium in the sample | direct |
| [mean_frict_vel](mean_frict_vel.md) | 0..1 <br/> [String](String.md) | Measurement of mean friction velocity | direct |
| [mean_peak_frict_vel](mean_peak_frict_vel.md) | 0..1 <br/> [String](String.md) | Measurement of mean peak friction velocity | direct |
| [misc_param](misc_param.md) | 0..* <br/> [String](String.md) | Any other measurement performed or parameter collected, that is not listed he... | direct |
| [n_alkanes](n_alkanes.md) | 0..* <br/> [String](String.md) | Concentration of n-alkanes; can include multiple n-alkanes | direct |
| [nitrate](nitrate.md) | 0..1 <br/> [String](String.md) | Concentration of nitrate in the sample | direct |
| [nitrite](nitrite.md) | 0..1 <br/> [String](String.md) | Concentration of nitrite in the sample | direct |
| [nitro](nitro.md) | 0..1 <br/> [String](String.md) | Concentration of nitrogen (total) | direct |
| [org_carb](org_carb.md) | 0..1 <br/> [String](String.md) | Concentration of organic carbon | direct |
| [org_matter](org_matter.md) | 0..1 <br/> [String](String.md) | Concentration of organic matter | direct |
| [org_nitro](org_nitro.md) | 0..1 <br/> [String](String.md) | Concentration of organic nitrogen | direct |
| [organism_count](organism_count.md) | 0..* <br/> [String](String.md) | Total cell count of any organism (or group of organisms) per gram, volume or ... | direct |
| [oxy_stat_samp](oxy_stat_samp.md) | 0..1 <br/> [OXYSTATSAMPENUM](OXYSTATSAMPENUM.md) | Oxygenation status of sample | direct |
| [ph](ph.md) | 0..1 <br/> [Float](Float.md) | Ph measurement of the sample, or liquid portion of sample, or aqueous phase o... | direct |
| [part_org_carb](part_org_carb.md) | 0..1 <br/> [String](String.md) | Concentration of particulate organic carbon | direct |
| [part_org_nitro](part_org_nitro.md) | 0..1 <br/> [String](String.md) | Concentration of particulate organic nitrogen | direct |
| [perturbation](perturbation.md) | 0..* <br/> [String](String.md) | Type of perturbation, e | direct |
| [petroleum_hydrocarb](petroleum_hydrocarb.md) | 0..1 <br/> [String](String.md) | Concentration of petroleum hydrocarbon | direct |
| [phaeopigments](phaeopigments.md) | 0..* <br/> [String](String.md) | Concentration of phaeopigments; can include multiple phaeopigments | direct |
| [phosphate](phosphate.md) | 0..1 <br/> [String](String.md) | Concentration of phosphate | direct |
| [phosplipid_fatt_acid](phosplipid_fatt_acid.md) | 0..* <br/> [String](String.md) | Concentration of phospholipid fatty acids; can include multiple values | direct |
| [photon_flux](photon_flux.md) | 0..1 <br/> [String](String.md) | Measurement of photon flux | direct |
| [potassium](potassium.md) | 0..1 <br/> [String](String.md) | Concentration of potassium in the sample | direct |
| [pressure](pressure.md) | 0..1 <br/> [String](String.md) | Pressure to which the sample is subject to, in atmospheres | direct |
| [primary_prod](primary_prod.md) | 0..1 <br/> [String](String.md) | Measurement of primary production, generally measured as isotope uptake | direct |
| [redox_potential](redox_potential.md) | 0..1 <br/> [String](String.md) | Redox potential, measured relative to a hydrogen cell, indicating oxidation o... | direct |
| [salinity](salinity.md) | 0..1 <br/> [String](String.md) | The total concentration of all dissolved salts in a liquid or solid sample | direct |
| [samp_store_dur](samp_store_dur.md) | 0..1 <br/> [String](String.md) | Duration for which the sample was stored | direct |
| [samp_store_loc](samp_store_loc.md) | 0..1 <br/> [String](String.md) | Location at which sample was stored, usually name of a specific freezer/room | direct |
| [samp_store_temp](samp_store_temp.md) | 0..1 <br/> [String](String.md) | Temperature at which sample was stored, e | direct |
| [samp_vol_we_dna_ext](samp_vol_we_dna_ext.md) | 0..1 <br/> [String](String.md) | Volume (ml) or mass (g) of total collected sample processed for DNA extractio... | direct |
| [silicate](silicate.md) | 0..1 <br/> [String](String.md) | Concentration of silicate | direct |
| [size_frac_low](size_frac_low.md) | 0..1 <br/> [String](String.md) | Refers to the mesh/pore size used to pre-filter/pre-sort the sample | direct |
| [size_frac_up](size_frac_up.md) | 0..1 <br/> [String](String.md) | Refers to the mesh/pore size used to retain the sample | direct |
| [sodium](sodium.md) | 0..1 <br/> [String](String.md) | Sodium concentration in the sample | direct |
| [soluble_react_phosp](soluble_react_phosp.md) | 0..1 <br/> [String](String.md) | Concentration of soluble reactive phosphorus | direct |
| [sulfate](sulfate.md) | 0..1 <br/> [String](String.md) | Concentration of sulfate in the sample | direct |
| [sulfide](sulfide.md) | 0..1 <br/> [String](String.md) | Concentration of sulfide in the sample | direct |
| [suspend_part_matter](suspend_part_matter.md) | 0..1 <br/> [String](String.md) | Concentration of suspended particulate matter | direct |
| [temp](temp.md) | 0..1 <br/> [String](String.md) | Temperature of the sample at the time of sampling | direct |
| [tidal_stage](tidal_stage.md) | 0..1 <br/> [TIDALSTAGEENUM](TIDALSTAGEENUM.md) | Stage of tide | direct |
| [tot_depth_water_col](tot_depth_water_col.md) | 0..1 <br/> [String](String.md) | Measurement of total depth of water column | direct |
| [tot_diss_nitro](tot_diss_nitro.md) | 0..1 <br/> [String](String.md) | Total dissolved nitrogen concentration, reported as nitrogen, measured by: to... | direct |
| [tot_inorg_nitro](tot_inorg_nitro.md) | 0..1 <br/> [String](String.md) | Total inorganic nitrogen content | direct |
| [tot_nitro](tot_nitro.md) | 0..1 <br/> [String](String.md) | Total nitrogen concentration of water samples, calculated by: total nitrogen ... | direct |
| [tot_part_carb](tot_part_carb.md) | 0..1 <br/> [String](String.md) | Total particulate carbon content | direct |
| [tot_phosp](tot_phosp.md) | 0..1 <br/> [String](String.md) | Total phosphorus concentration in the sample, calculated by: total phosphorus... | direct |
| [turbidity](turbidity.md) | 0..1 <br/> [String](String.md) | Measure of the amount of cloudiness or haziness in water caused by individual... | direct |
| [water_current](water_current.md) | 0..1 <br/> [String](String.md) | Measurement of magnitude and direction of flow within a fluid | direct |









## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mixs_6_2_proposal:Water |
| native | mixs_6_2_proposal:Water |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Water
title: Water
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
is_a: EnvironmentalPackage
mixin: false
slots:
- samp_name
- project_name
- depth
- elev
- alkalinity
- alkalinity_method
- alkyl_diethers
- aminopept_act
- ammonium
- atmospheric_data
- bacteria_carb_prod
- bac_prod
- bac_resp
- biomass
- bishomohopanol
- bromide
- calcium
- carb_nitro_ratio
- chem_administration
- chloride
- chlorophyll
- conduc
- density
- diether_lipids
- diss_carb_dioxide
- diss_hydrogen
- diss_inorg_carb
- diss_inorg_nitro
- diss_inorg_phosp
- diss_org_carb
- diss_org_nitro
- diss_oxygen
- down_par
- fluor
- glucosidase_act
- light_intensity
- magnesium
- mean_frict_vel
- mean_peak_frict_vel
- misc_param
- n_alkanes
- nitrate
- nitrite
- nitro
- org_carb
- org_matter
- org_nitro
- organism_count
- oxy_stat_samp
- ph
- part_org_carb
- part_org_nitro
- perturbation
- petroleum_hydrocarb
- phaeopigments
- phosphate
- phosplipid_fatt_acid
- photon_flux
- potassium
- pressure
- primary_prod
- redox_potential
- salinity
- samp_store_dur
- samp_store_loc
- samp_store_temp
- samp_vol_we_dna_ext
- silicate
- size_frac_low
- size_frac_up
- sodium
- soluble_react_phosp
- sulfate
- sulfide
- suspend_part_matter
- temp
- tidal_stage
- tot_depth_water_col
- tot_diss_nitro
- tot_inorg_nitro
- tot_nitro
- tot_part_carb
- tot_phosp
- turbidity
- water_current
slot_usage:
  alkyl_diethers:
    name: alkyl_diethers
    domain_of:
    - MicrobialMatBiofilm
    - Sediment
    - Water
  ammonium:
    name: ammonium
    domain_of:
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Water
    required: false
    recommended: false
  bacteria_carb_prod:
    name: bacteria_carb_prod
    domain_of:
    - MicrobialMatBiofilm
    - Sediment
    - Water
  carb_nitro_ratio:
    name: carb_nitro_ratio
    string_serialization: '{float}:{float}'
    domain_of:
    - MicrobialMatBiofilm
    - Sediment
    - Water
  chem_administration:
    name: chem_administration
    domain_of:
    - Agriculture
    - Air
    - FoodFarmEnvironment
    - HostAssociated
    - HumanAssociated
    - HumanGut
    - HumanOral
    - HumanSkin
    - HumanVaginal
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - PlantAssociated
    - Sediment
    - SymbiontAssociated
    - WastewaterSludge
    - Water
    required: false
    recommended: false
  density:
    name: density
    domain_of:
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Water
  depth:
    name: depth
    title: depth
    examples:
    - value: 10 meter
    domain_of:
    - Agriculture
    - FoodFarmEnvironment
    - HostAssociated
    - MicrobialMatBiofilm
    - MigsBa
    - MigsEu
    - MigsOrg
    - MigsPl
    - MigsVi
    - Mimag
    - MimarksC
    - MimarksS
    - Mims
    - Misag
    - MiscellaneousNaturalOrArtificialEnvironment
    - Miuvig
    - PlantAssociated
    - Sediment
    - Soil
    - SymbiontAssociated
    - WastewaterSludge
    - Water
    required: true
  diss_inorg_carb:
    name: diss_inorg_carb
    domain_of:
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Water
  diss_inorg_phosp:
    name: diss_inorg_phosp
    domain_of:
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - Water
    required: false
    recommended: false
  diss_org_nitro:
    name: diss_org_nitro
    domain_of:
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Water
  elev:
    name: elev
    domain_of:
    - Agriculture
    - Air
    - HostAssociated
    - HydrocarbonResourcesCores
    - MicrobialMatBiofilm
    - MigsBa
    - MigsEu
    - MigsOrg
    - MigsPl
    - MigsVi
    - Mimag
    - MimarksC
    - MimarksS
    - Mims
    - Misag
    - MiscellaneousNaturalOrArtificialEnvironment
    - Miuvig
    - PlantAssociated
    - Sediment
    - Soil
    - SymbiontAssociated
    - Water
    recommended: true
  misc_param:
    name: misc_param
    domain_of:
    - Agriculture
    - Air
    - FoodAnimalAndAnimalFeed
    - FoodFarmEnvironment
    - FoodFoodProductionFacility
    - FoodHumanFoods
    - HostAssociated
    - HumanAssociated
    - HumanGut
    - HumanOral
    - HumanSkin
    - HumanVaginal
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - PlantAssociated
    - Sediment
    - Soil
    - SymbiontAssociated
    - WastewaterSludge
    - Water
  n_alkanes:
    name: n_alkanes
    domain_of:
    - MicrobialMatBiofilm
    - Sediment
    - Water
  nitrate:
    name: nitrate
    domain_of:
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - WastewaterSludge
    - Water
    required: false
    recommended: false
  nitrite:
    name: nitrite
    domain_of:
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Water
    required: false
    recommended: false
  org_carb:
    name: org_carb
    domain_of:
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Water
  org_matter:
    name: org_matter
    domain_of:
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Soil
    - Water
  org_nitro:
    name: org_nitro
    domain_of:
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Soil
    - Water
  organism_count:
    name: organism_count
    description: 'Total cell count of any organism (or group of organisms) per gram,
      volume or area of sample, should include name of organism followed by count.
      The method that was used for the enumeration (e.g. qPCR, atp, mpn, etc.) Should
      also be provided. (example: total prokaryotes; 3.5e7 cells per ml; qpcr)'
    examples:
    - value: total prokaryotes;3.5e7 cells per milliliter;qPCR
    string_serialization: '{text};{float} {unit};[qPCR|ATP|MPN|other]'
    multivalued: true
    domain_of:
    - Agriculture
    - Air
    - BuiltEnvironment
    - FoodAnimalAndAnimalFeed
    - FoodFarmEnvironment
    - FoodFoodProductionFacility
    - FoodHumanFoods
    - HostAssociated
    - HumanAssociated
    - HumanGut
    - HumanOral
    - HumanSkin
    - HumanVaginal
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - PlantAssociated
    - Sediment
    - SymbiontAssociated
    - WastewaterSludge
    - Water
    required: false
    recommended: false
  oxy_stat_samp:
    name: oxy_stat_samp
    domain_of:
    - Agriculture
    - Air
    - HostAssociated
    - HumanAssociated
    - HumanGut
    - HumanOral
    - HumanSkin
    - HumanVaginal
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - PlantAssociated
    - Sediment
    - SymbiontAssociated
    - WastewaterSludge
    - Water
    required: false
    recommended: false
  part_org_carb:
    name: part_org_carb
    domain_of:
    - MicrobialMatBiofilm
    - Sediment
    - Water
  perturbation:
    name: perturbation
    string_serialization: '{text};{Rn/start_time/end_time/duration}'
    domain_of:
    - Agriculture
    - Air
    - FoodAnimalAndAnimalFeed
    - FoodFarmEnvironment
    - FoodHumanFoods
    - HostAssociated
    - HumanAssociated
    - HumanGut
    - HumanOral
    - HumanSkin
    - HumanVaginal
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - PlantAssociated
    - Sediment
    - SymbiontAssociated
    - WastewaterSludge
    - Water
    required: false
    recommended: false
  ph:
    name: ph
    description: Ph measurement of the sample, or liquid portion of sample, or aqueous
      phase of the fluid
    domain_of:
    - FoodFarmEnvironment
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Soil
    - WastewaterSludge
    - Water
    required: false
    recommended: false
  phosplipid_fatt_acid:
    name: phosplipid_fatt_acid
    domain_of:
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Water
  salinity:
    name: salinity
    multivalued: false
    domain_of:
    - Air
    - FoodFarmEnvironment
    - HostAssociated
    - HumanAssociated
    - HumanGut
    - HumanOral
    - HumanSkin
    - HumanVaginal
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - PlantAssociated
    - Sediment
    - SymbiontAssociated
    - WastewaterSludge
    - Water
  samp_store_dur:
    name: samp_store_dur
    description: Duration for which the sample was stored
    string_serialization: '{duration}'
    domain_of:
    - Agriculture
    - Air
    - FoodAnimalAndAnimalFeed
    - FoodFarmEnvironment
    - FoodFoodProductionFacility
    - FoodHumanFoods
    - HostAssociated
    - HumanAssociated
    - HumanGut
    - HumanOral
    - HumanSkin
    - HumanVaginal
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - PlantAssociated
    - Sediment
    - SymbiontAssociated
    - WastewaterSludge
    - Water
    required: false
    recommended: false
  samp_store_loc:
    name: samp_store_loc
    description: Location at which sample was stored, usually name of a specific freezer/room
    examples:
    - value: Freezer no:5
    domain_of:
    - Agriculture
    - Air
    - FoodAnimalAndAnimalFeed
    - FoodFoodProductionFacility
    - FoodHumanFoods
    - HostAssociated
    - HumanAssociated
    - HumanGut
    - HumanOral
    - HumanSkin
    - HumanVaginal
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - PlantAssociated
    - Sediment
    - SymbiontAssociated
    - WastewaterSludge
    - Water
    required: false
    recommended: false
  samp_vol_we_dna_ext:
    name: samp_vol_we_dna_ext
    description: 'Volume (ml) or mass (g) of total collected sample processed for
      DNA extraction. Note: total sample collected should be entered under the term
      Sample Size (MIXS:0000001).'
    domain_of:
    - Agriculture
    - Air
    - FoodAnimalAndAnimalFeed
    - FoodFarmEnvironment
    - FoodFoodProductionFacility
    - FoodHumanFoods
    - HostAssociated
    - HumanAssociated
    - HumanGut
    - HumanOral
    - HumanSkin
    - HumanVaginal
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MigsBa
    - MigsEu
    - MigsOrg
    - MigsPl
    - MigsVi
    - Mimag
    - MimarksC
    - MimarksS
    - Mims
    - Misag
    - MiscellaneousNaturalOrArtificialEnvironment
    - Miuvig
    - PlantAssociated
    - Sediment
    - Soil
    - SymbiontAssociated
    - WastewaterSludge
    - Water
    required: false
    recommended: false
  sulfate:
    name: sulfate
    domain_of:
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Water
    required: false
    recommended: false
  sulfide:
    name: sulfide
    domain_of:
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Water
    required: false
    recommended: false
  temp:
    name: temp
    domain_of:
    - Agriculture
    - Air
    - FoodAnimalAndAnimalFeed
    - FoodFarmEnvironment
    - FoodHumanFoods
    - HostAssociated
    - HumanAssociated
    - HumanGut
    - HumanOral
    - HumanSkin
    - HumanVaginal
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MigsBa
    - MigsEu
    - MigsOrg
    - MigsPl
    - MigsVi
    - Mimag
    - MimarksC
    - MimarksS
    - Mims
    - Misag
    - MiscellaneousNaturalOrArtificialEnvironment
    - Miuvig
    - PlantAssociated
    - Sediment
    - Soil
    - SymbiontAssociated
    - WastewaterSludge
    - Water
    required: false
    recommended: false
  tot_phosp:
    name: tot_phosp
    title: total phosphorus
    domain_of:
    - Agriculture
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - Water
    required: false
    recommended: false
  turbidity:
    name: turbidity
    domain_of:
    - FoodFarmEnvironment
    - MicrobialMatBiofilm
    - Sediment
    - Water

```
</details>

### Induced

<details>
```yaml
name: Water
title: Water
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
is_a: EnvironmentalPackage
mixin: false
slot_usage:
  alkyl_diethers:
    name: alkyl_diethers
    domain_of:
    - MicrobialMatBiofilm
    - Sediment
    - Water
  ammonium:
    name: ammonium
    domain_of:
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Water
    required: false
    recommended: false
  bacteria_carb_prod:
    name: bacteria_carb_prod
    domain_of:
    - MicrobialMatBiofilm
    - Sediment
    - Water
  carb_nitro_ratio:
    name: carb_nitro_ratio
    string_serialization: '{float}:{float}'
    domain_of:
    - MicrobialMatBiofilm
    - Sediment
    - Water
  chem_administration:
    name: chem_administration
    domain_of:
    - Agriculture
    - Air
    - FoodFarmEnvironment
    - HostAssociated
    - HumanAssociated
    - HumanGut
    - HumanOral
    - HumanSkin
    - HumanVaginal
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - PlantAssociated
    - Sediment
    - SymbiontAssociated
    - WastewaterSludge
    - Water
    required: false
    recommended: false
  density:
    name: density
    domain_of:
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Water
  depth:
    name: depth
    title: depth
    examples:
    - value: 10 meter
    domain_of:
    - Agriculture
    - FoodFarmEnvironment
    - HostAssociated
    - MicrobialMatBiofilm
    - MigsBa
    - MigsEu
    - MigsOrg
    - MigsPl
    - MigsVi
    - Mimag
    - MimarksC
    - MimarksS
    - Mims
    - Misag
    - MiscellaneousNaturalOrArtificialEnvironment
    - Miuvig
    - PlantAssociated
    - Sediment
    - Soil
    - SymbiontAssociated
    - WastewaterSludge
    - Water
    required: true
  diss_inorg_carb:
    name: diss_inorg_carb
    domain_of:
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Water
  diss_inorg_phosp:
    name: diss_inorg_phosp
    domain_of:
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - Water
    required: false
    recommended: false
  diss_org_nitro:
    name: diss_org_nitro
    domain_of:
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Water
  elev:
    name: elev
    domain_of:
    - Agriculture
    - Air
    - HostAssociated
    - HydrocarbonResourcesCores
    - MicrobialMatBiofilm
    - MigsBa
    - MigsEu
    - MigsOrg
    - MigsPl
    - MigsVi
    - Mimag
    - MimarksC
    - MimarksS
    - Mims
    - Misag
    - MiscellaneousNaturalOrArtificialEnvironment
    - Miuvig
    - PlantAssociated
    - Sediment
    - Soil
    - SymbiontAssociated
    - Water
    recommended: true
  misc_param:
    name: misc_param
    domain_of:
    - Agriculture
    - Air
    - FoodAnimalAndAnimalFeed
    - FoodFarmEnvironment
    - FoodFoodProductionFacility
    - FoodHumanFoods
    - HostAssociated
    - HumanAssociated
    - HumanGut
    - HumanOral
    - HumanSkin
    - HumanVaginal
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - PlantAssociated
    - Sediment
    - Soil
    - SymbiontAssociated
    - WastewaterSludge
    - Water
  n_alkanes:
    name: n_alkanes
    domain_of:
    - MicrobialMatBiofilm
    - Sediment
    - Water
  nitrate:
    name: nitrate
    domain_of:
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - WastewaterSludge
    - Water
    required: false
    recommended: false
  nitrite:
    name: nitrite
    domain_of:
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Water
    required: false
    recommended: false
  org_carb:
    name: org_carb
    domain_of:
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Water
  org_matter:
    name: org_matter
    domain_of:
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Soil
    - Water
  org_nitro:
    name: org_nitro
    domain_of:
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Soil
    - Water
  organism_count:
    name: organism_count
    description: 'Total cell count of any organism (or group of organisms) per gram,
      volume or area of sample, should include name of organism followed by count.
      The method that was used for the enumeration (e.g. qPCR, atp, mpn, etc.) Should
      also be provided. (example: total prokaryotes; 3.5e7 cells per ml; qpcr)'
    examples:
    - value: total prokaryotes;3.5e7 cells per milliliter;qPCR
    string_serialization: '{text};{float} {unit};[qPCR|ATP|MPN|other]'
    multivalued: true
    domain_of:
    - Agriculture
    - Air
    - BuiltEnvironment
    - FoodAnimalAndAnimalFeed
    - FoodFarmEnvironment
    - FoodFoodProductionFacility
    - FoodHumanFoods
    - HostAssociated
    - HumanAssociated
    - HumanGut
    - HumanOral
    - HumanSkin
    - HumanVaginal
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - PlantAssociated
    - Sediment
    - SymbiontAssociated
    - WastewaterSludge
    - Water
    required: false
    recommended: false
  oxy_stat_samp:
    name: oxy_stat_samp
    domain_of:
    - Agriculture
    - Air
    - HostAssociated
    - HumanAssociated
    - HumanGut
    - HumanOral
    - HumanSkin
    - HumanVaginal
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - PlantAssociated
    - Sediment
    - SymbiontAssociated
    - WastewaterSludge
    - Water
    required: false
    recommended: false
  part_org_carb:
    name: part_org_carb
    domain_of:
    - MicrobialMatBiofilm
    - Sediment
    - Water
  perturbation:
    name: perturbation
    string_serialization: '{text};{Rn/start_time/end_time/duration}'
    domain_of:
    - Agriculture
    - Air
    - FoodAnimalAndAnimalFeed
    - FoodFarmEnvironment
    - FoodHumanFoods
    - HostAssociated
    - HumanAssociated
    - HumanGut
    - HumanOral
    - HumanSkin
    - HumanVaginal
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - PlantAssociated
    - Sediment
    - SymbiontAssociated
    - WastewaterSludge
    - Water
    required: false
    recommended: false
  ph:
    name: ph
    description: Ph measurement of the sample, or liquid portion of sample, or aqueous
      phase of the fluid
    domain_of:
    - FoodFarmEnvironment
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Soil
    - WastewaterSludge
    - Water
    required: false
    recommended: false
  phosplipid_fatt_acid:
    name: phosplipid_fatt_acid
    domain_of:
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Water
  salinity:
    name: salinity
    multivalued: false
    domain_of:
    - Air
    - FoodFarmEnvironment
    - HostAssociated
    - HumanAssociated
    - HumanGut
    - HumanOral
    - HumanSkin
    - HumanVaginal
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - PlantAssociated
    - Sediment
    - SymbiontAssociated
    - WastewaterSludge
    - Water
  samp_store_dur:
    name: samp_store_dur
    description: Duration for which the sample was stored
    string_serialization: '{duration}'
    domain_of:
    - Agriculture
    - Air
    - FoodAnimalAndAnimalFeed
    - FoodFarmEnvironment
    - FoodFoodProductionFacility
    - FoodHumanFoods
    - HostAssociated
    - HumanAssociated
    - HumanGut
    - HumanOral
    - HumanSkin
    - HumanVaginal
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - PlantAssociated
    - Sediment
    - SymbiontAssociated
    - WastewaterSludge
    - Water
    required: false
    recommended: false
  samp_store_loc:
    name: samp_store_loc
    description: Location at which sample was stored, usually name of a specific freezer/room
    examples:
    - value: Freezer no:5
    domain_of:
    - Agriculture
    - Air
    - FoodAnimalAndAnimalFeed
    - FoodFoodProductionFacility
    - FoodHumanFoods
    - HostAssociated
    - HumanAssociated
    - HumanGut
    - HumanOral
    - HumanSkin
    - HumanVaginal
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - PlantAssociated
    - Sediment
    - SymbiontAssociated
    - WastewaterSludge
    - Water
    required: false
    recommended: false
  samp_vol_we_dna_ext:
    name: samp_vol_we_dna_ext
    description: 'Volume (ml) or mass (g) of total collected sample processed for
      DNA extraction. Note: total sample collected should be entered under the term
      Sample Size (MIXS:0000001).'
    domain_of:
    - Agriculture
    - Air
    - FoodAnimalAndAnimalFeed
    - FoodFarmEnvironment
    - FoodFoodProductionFacility
    - FoodHumanFoods
    - HostAssociated
    - HumanAssociated
    - HumanGut
    - HumanOral
    - HumanSkin
    - HumanVaginal
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MigsBa
    - MigsEu
    - MigsOrg
    - MigsPl
    - MigsVi
    - Mimag
    - MimarksC
    - MimarksS
    - Mims
    - Misag
    - MiscellaneousNaturalOrArtificialEnvironment
    - Miuvig
    - PlantAssociated
    - Sediment
    - Soil
    - SymbiontAssociated
    - WastewaterSludge
    - Water
    required: false
    recommended: false
  sulfate:
    name: sulfate
    domain_of:
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Water
    required: false
    recommended: false
  sulfide:
    name: sulfide
    domain_of:
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Water
    required: false
    recommended: false
  temp:
    name: temp
    domain_of:
    - Agriculture
    - Air
    - FoodAnimalAndAnimalFeed
    - FoodFarmEnvironment
    - FoodHumanFoods
    - HostAssociated
    - HumanAssociated
    - HumanGut
    - HumanOral
    - HumanSkin
    - HumanVaginal
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MigsBa
    - MigsEu
    - MigsOrg
    - MigsPl
    - MigsVi
    - Mimag
    - MimarksC
    - MimarksS
    - Mims
    - Misag
    - MiscellaneousNaturalOrArtificialEnvironment
    - Miuvig
    - PlantAssociated
    - Sediment
    - Soil
    - SymbiontAssociated
    - WastewaterSludge
    - Water
    required: false
    recommended: false
  tot_phosp:
    name: tot_phosp
    title: total phosphorus
    domain_of:
    - Agriculture
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - Water
    required: false
    recommended: false
  turbidity:
    name: turbidity
    domain_of:
    - FoodFarmEnvironment
    - MicrobialMatBiofilm
    - Sediment
    - Water
attributes:
  samp_name:
    name: samp_name
    description: A local identifier or name that for the material sample used for
      extracting nucleic acids, and subsequent sequencing. It can refer either to
      the original material collected or to any derived sub-samples. It can have any
      format, but we suggest that you make it concise, unique and consistent within
      your lab, and as informative as possible. INSDC requires every sample name from
      a single Submitter to be unique. Use of a globally unique identifier for the
      field source_mat_id is recommended in addition to sample_name
    title: sample name
    notes:
    - sample
    examples:
    - value: ISDsoil1
    in_subset:
    - investigation
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0001107
    multivalued: false
    alias: samp_name
    owner: Water
    domain_of:
    - Air
    - BuiltEnvironment
    - FoodAnimalAndAnimalFeed
    - FoodFarmEnvironment
    - FoodFoodProductionFacility
    - FoodHumanFoods
    - HostAssociated
    - HumanAssociated
    - HumanGut
    - HumanOral
    - HumanSkin
    - HumanVaginal
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MigsBa
    - MigsEu
    - MigsOrg
    - MigsPl
    - MigsVi
    - Mimag
    - MimarksC
    - MimarksS
    - Mims
    - Misag
    - MiscellaneousNaturalOrArtificialEnvironment
    - Miuvig
    - PlantAssociated
    - Sediment
    - Soil
    - SymbiontAssociated
    - WastewaterSludge
    - Water
    range: string
    required: true
  project_name:
    name: project_name
    description: Name of the project within which the sequencing was organized
    title: project name
    notes:
    - project
    examples:
    - value: Forest soil metagenome
    in_subset:
    - investigation
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000092
    multivalued: false
    alias: project_name
    owner: Water
    domain_of:
    - Air
    - BuiltEnvironment
    - FoodAnimalAndAnimalFeed
    - FoodFarmEnvironment
    - FoodFoodProductionFacility
    - FoodHumanFoods
    - HostAssociated
    - HumanAssociated
    - HumanGut
    - HumanOral
    - HumanSkin
    - HumanVaginal
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MigsBa
    - MigsEu
    - MigsOrg
    - MigsPl
    - MigsVi
    - Mimag
    - MimarksC
    - MimarksS
    - Mims
    - Misag
    - MiscellaneousNaturalOrArtificialEnvironment
    - Miuvig
    - PlantAssociated
    - Sediment
    - Soil
    - SymbiontAssociated
    - WastewaterSludge
    - Water
    range: string
    required: true
  depth:
    name: depth
    description: The vertical distance below local surface. For sediment or soil samples
      depth is measured from sediment or soil surface, respectively. Depth can be
      reported as an interval for subsurface samples
    title: depth
    examples:
    - value: 10 meter
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000018
    multivalued: false
    alias: depth
    owner: Water
    domain_of:
    - Agriculture
    - FoodFarmEnvironment
    - HostAssociated
    - MicrobialMatBiofilm
    - MigsBa
    - MigsEu
    - MigsOrg
    - MigsPl
    - MigsVi
    - Mimag
    - MimarksC
    - MimarksS
    - Mims
    - Misag
    - MiscellaneousNaturalOrArtificialEnvironment
    - Miuvig
    - PlantAssociated
    - Sediment
    - Soil
    - SymbiontAssociated
    - WastewaterSludge
    - Water
    range: string
    required: true
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  elev:
    name: elev
    description: Elevation of the sampling site is its height above a fixed reference
      point, most commonly the mean sea level. Elevation is mainly used when referring
      to points on the earth's surface, while altitude is used for points above the
      surface, such as an aircraft in flight or a spacecraft in orbit
    title: elevation
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000093
    multivalued: false
    alias: elev
    owner: Water
    domain_of:
    - Agriculture
    - Air
    - HostAssociated
    - HydrocarbonResourcesCores
    - MicrobialMatBiofilm
    - MigsBa
    - MigsEu
    - MigsOrg
    - MigsPl
    - MigsVi
    - Mimag
    - MimarksC
    - MimarksS
    - Mims
    - Misag
    - MiscellaneousNaturalOrArtificialEnvironment
    - Miuvig
    - PlantAssociated
    - Sediment
    - Soil
    - SymbiontAssociated
    - Water
    range: string
    recommended: true
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  alkalinity:
    name: alkalinity
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: milliequivalent per liter, milligram per liter
    description: Alkalinity, the ability of a solution to neutralize acids to the
      equivalence point of carbonate or bicarbonate
    title: alkalinity
    notes:
    - alkalinity
    examples:
    - value: 50 milligram per liter
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000421
    multivalued: false
    alias: alkalinity
    owner: Water
    domain_of:
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - WastewaterSludge
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  alkalinity_method:
    name: alkalinity_method
    description: Method used for alkalinity measurement
    title: alkalinity method
    notes:
    - alkalinity
    - method
    examples:
    - value: titration
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000298
    multivalued: false
    alias: alkalinity_method
    owner: Water
    domain_of:
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - Water
    range: string
    required: false
    recommended: false
  alkyl_diethers:
    name: alkyl_diethers
    description: Concentration of alkyl diethers
    title: alkyl diethers
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000490
    multivalued: false
    alias: alkyl_diethers
    owner: Water
    domain_of:
    - MicrobialMatBiofilm
    - Sediment
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  aminopept_act:
    name: aminopept_act
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: mole per liter per hour
    description: Measurement of aminopeptidase activity
    title: aminopeptidase activity
    examples:
    - value: 0.269 mole per liter per hour
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000172
    multivalued: false
    alias: aminopept_act
    owner: Water
    domain_of:
    - MicrobialMatBiofilm
    - Sediment
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  ammonium:
    name: ammonium
    description: Concentration of ammonium in the sample
    title: ammonium
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000427
    multivalued: false
    alias: ammonium
    owner: Water
    domain_of:
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  atmospheric_data:
    name: atmospheric_data
    annotations:
      Expected_value:
        tag: Expected_value
        value: atmospheric data name;measurement value
    description: Measurement of atmospheric data; can include multiple data
    title: atmospheric data
    examples:
    - value: wind speed;9 knots
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    string_serialization: '{text};{float} {unit}'
    slot_uri: MIXS:0001097
    multivalued: true
    alias: atmospheric_data
    owner: Water
    domain_of:
    - Water
    range: string
    required: false
    recommended: false
  bacteria_carb_prod:
    name: bacteria_carb_prod
    description: Measurement of bacterial carbon production
    title: bacterial carbon production
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000173
    multivalued: false
    alias: bacteria_carb_prod
    owner: Water
    domain_of:
    - MicrobialMatBiofilm
    - Sediment
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  bac_prod:
    name: bac_prod
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: milligram per cubic meter per day
    description: Bacterial production in the water column measured by isotope uptake
    title: bacterial production
    notes:
    - production
    examples:
    - value: 5 milligram per cubic meter per day
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000683
    multivalued: false
    alias: bac_prod
    owner: Water
    domain_of:
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  bac_resp:
    name: bac_resp
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: milligram per cubic meter per day, micromole oxygen per liter per hour
    description: Measurement of bacterial respiration in the water column
    title: bacterial respiration
    examples:
    - value: 300 micromole oxygen per liter per hour
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000684
    multivalued: false
    alias: bac_resp
    owner: Water
    domain_of:
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  biomass:
    name: biomass
    annotations:
      Expected_value:
        tag: Expected_value
        value: biomass type;measurement value
      Preferred_unit:
        tag: Preferred_unit
        value: ton, kilogram, gram
    description: Amount of biomass; should include the name for the part of biomass
      measured, e.g. Microbial, total. Can include multiple measurements
    title: biomass
    notes:
    - biomass
    examples:
    - value: total;20 gram
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    string_serialization: '{text};{float} {unit}'
    slot_uri: MIXS:0000174
    multivalued: true
    alias: biomass
    owner: Water
    domain_of:
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Water
    range: string
    required: false
    recommended: false
  bishomohopanol:
    name: bishomohopanol
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: microgram per liter, microgram per gram
    description: Concentration of bishomohopanol
    title: bishomohopanol
    examples:
    - value: 14 microgram per liter
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000175
    multivalued: false
    alias: bishomohopanol
    owner: Water
    domain_of:
    - MicrobialMatBiofilm
    - Sediment
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  bromide:
    name: bromide
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: parts per million
    description: Concentration of bromide
    title: bromide
    examples:
    - value: 0.05 parts per million
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000176
    multivalued: false
    alias: bromide
    owner: Water
    domain_of:
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  calcium:
    name: calcium
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: milligram per liter, micromole per liter, parts per million
    description: Concentration of calcium in the sample
    title: calcium
    examples:
    - value: 0.2 micromole per liter
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000432
    multivalued: false
    alias: calcium
    owner: Water
    domain_of:
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  carb_nitro_ratio:
    name: carb_nitro_ratio
    description: Ratio of amount or concentrations of carbon to nitrogen
    title: carbon/nitrogen ratio
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    string_serialization: '{float}:{float}'
    slot_uri: MIXS:0000310
    alias: carb_nitro_ratio
    owner: Water
    domain_of:
    - MicrobialMatBiofilm
    - Sediment
    - Water
    range: float
    required: false
    recommended: false
  chem_administration:
    name: chem_administration
    description: List of chemical compounds administered to the host or site where
      sampling occurred, and when (e.g. Antibiotics, n fertilizer, air filter); can
      include multiple compounds. For chemical entities of biological interest ontology
      (chebi) (v 163), http://purl.bioontology.org/ontology/chebi
    title: chemical administration
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    string_serialization: '{termLabel} [{termID}];{timestamp}'
    slot_uri: MIXS:0000751
    multivalued: true
    alias: chem_administration
    owner: Water
    domain_of:
    - Agriculture
    - Air
    - FoodFarmEnvironment
    - HostAssociated
    - HumanAssociated
    - HumanGut
    - HumanOral
    - HumanSkin
    - HumanVaginal
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - PlantAssociated
    - Sediment
    - SymbiontAssociated
    - WastewaterSludge
    - Water
    range: string
    required: false
    recommended: false
  chloride:
    name: chloride
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: milligram per liter, parts per million
    description: Concentration of chloride in the sample
    title: chloride
    examples:
    - value: 5000 milligram per liter
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000429
    multivalued: false
    alias: chloride
    owner: Water
    domain_of:
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  chlorophyll:
    name: chlorophyll
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: milligram per cubic meter, microgram per liter
    description: Concentration of chlorophyll
    title: chlorophyll
    examples:
    - value: 5 milligram per cubic meter
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000177
    multivalued: false
    alias: chlorophyll
    owner: Water
    domain_of:
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  conduc:
    name: conduc
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: milliSiemens per centimeter
    description: Electrical conductivity of water
    title: conductivity
    examples:
    - value: 10 milliSiemens per centimeter
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000692
    multivalued: false
    alias: conduc
    owner: Water
    domain_of:
    - FoodFarmEnvironment
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  density:
    name: density
    description: Density of the sample, which is its mass per unit volume (aka volumetric
      mass density)
    title: density
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000435
    multivalued: false
    alias: density
    owner: Water
    domain_of:
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  diether_lipids:
    name: diether_lipids
    annotations:
      Expected_value:
        tag: Expected_value
        value: diether lipid name;measurement value
      Preferred_unit:
        tag: Preferred_unit
        value: nanogram per liter
    description: Concentration of diether lipids; can include multiple types of diether
      lipids
    title: diether lipids
    examples:
    - value: 0.2 nanogram per liter
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    string_serialization: '{text};{float} {unit}'
    slot_uri: MIXS:0000178
    multivalued: true
    alias: diether_lipids
    owner: Water
    domain_of:
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Water
    range: string
    required: false
    recommended: false
  diss_carb_dioxide:
    name: diss_carb_dioxide
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: micromole per liter, milligram per liter
    description: Concentration of dissolved carbon dioxide in the sample or liquid
      portion of the sample
    title: dissolved carbon dioxide
    notes:
    - carbon
    - dissolved
    examples:
    - value: 5 milligram per liter
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000436
    multivalued: false
    alias: diss_carb_dioxide
    owner: Water
    domain_of:
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  diss_hydrogen:
    name: diss_hydrogen
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: micromole per liter
    description: Concentration of dissolved hydrogen
    title: dissolved hydrogen
    notes:
    - dissolved
    examples:
    - value: 0.3 micromole per liter
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000179
    multivalued: false
    alias: diss_hydrogen
    owner: Water
    domain_of:
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  diss_inorg_carb:
    name: diss_inorg_carb
    description: Dissolved inorganic carbon concentration in the sample, typically
      measured after filtering the sample using a 0.45 micrometer filter
    title: dissolved inorganic carbon
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000434
    multivalued: false
    alias: diss_inorg_carb
    owner: Water
    domain_of:
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  diss_inorg_nitro:
    name: diss_inorg_nitro
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: microgram per liter, micromole per liter
    description: Concentration of dissolved inorganic nitrogen
    title: dissolved inorganic nitrogen
    notes:
    - dissolved
    - inorganic
    - nitrogen
    examples:
    - value: 761 micromole per liter
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000698
    multivalued: false
    alias: diss_inorg_nitro
    owner: Water
    domain_of:
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  diss_inorg_phosp:
    name: diss_inorg_phosp
    description: Concentration of dissolved inorganic phosphorus in the sample
    title: dissolved inorganic phosphorus
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000106
    multivalued: false
    alias: diss_inorg_phosp
    owner: Water
    domain_of:
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  diss_org_carb:
    name: diss_org_carb
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: micromole per liter, milligram per liter
    description: Concentration of dissolved organic carbon in the sample, liquid portion
      of the sample, or aqueous phase of the fluid
    title: dissolved organic carbon
    notes:
    - carbon
    - dissolved
    - organic
    examples:
    - value: 197 micromole per liter
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000433
    multivalued: false
    alias: diss_org_carb
    owner: Water
    domain_of:
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - Sediment
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  diss_org_nitro:
    name: diss_org_nitro
    description: Dissolved organic nitrogen concentration measured as; total dissolved
      nitrogen - NH4 - NO3 - NO2
    title: dissolved organic nitrogen
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000162
    multivalued: false
    alias: diss_org_nitro
    owner: Water
    domain_of:
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  diss_oxygen:
    name: diss_oxygen
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: micromole per kilogram, milligram per liter
    description: Concentration of dissolved oxygen
    title: dissolved oxygen
    notes:
    - dissolved
    - oxygen
    examples:
    - value: 175 micromole per kilogram
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000119
    multivalued: false
    alias: diss_oxygen
    owner: Water
    domain_of:
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  down_par:
    name: down_par
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: microEinstein per square meter per second, microEinstein per square
          centimeter per second
    description: Visible waveband radiance and irradiance measurements in the water
      column
    title: downward PAR
    examples:
    - value: 28.71 microEinstein per square meter per second
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000703
    multivalued: false
    alias: down_par
    owner: Water
    domain_of:
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  fluor:
    name: fluor
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: milligram chlorophyll a per cubic meter, volts
    description: Raw or converted fluorescence of water
    title: fluorescence
    examples:
    - value: 2.5 volts
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000704
    multivalued: false
    alias: fluor
    owner: Water
    domain_of:
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  glucosidase_act:
    name: glucosidase_act
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: mol per liter per hour
    description: Measurement of glucosidase activity
    title: glucosidase activity
    examples:
    - value: 5 mol per liter per hour
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000137
    multivalued: false
    alias: glucosidase_act
    owner: Water
    domain_of:
    - MicrobialMatBiofilm
    - Sediment
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  light_intensity:
    name: light_intensity
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: lux
    description: Measurement of light intensity
    title: light intensity
    notes:
    - intensity
    - light
    examples:
    - value: 0.3 lux
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000706
    multivalued: false
    alias: light_intensity
    owner: Water
    domain_of:
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  magnesium:
    name: magnesium
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: mole per liter, milligram per liter, parts per million, micromole per
          kilogram
    description: Concentration of magnesium in the sample
    title: magnesium
    examples:
    - value: 52.8 micromole per kilogram
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000431
    multivalued: false
    alias: magnesium
    owner: Water
    domain_of:
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - Sediment
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  mean_frict_vel:
    name: mean_frict_vel
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: meter per second
    description: Measurement of mean friction velocity
    title: mean friction velocity
    notes:
    - mean
    - velocity
    examples:
    - value: 0.5 meter per second
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000498
    multivalued: false
    alias: mean_frict_vel
    owner: Water
    domain_of:
    - MicrobialMatBiofilm
    - Sediment
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  mean_peak_frict_vel:
    name: mean_peak_frict_vel
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: meter per second
    description: Measurement of mean peak friction velocity
    title: mean peak friction velocity
    notes:
    - mean
    - peak
    - velocity
    examples:
    - value: 1 meter per second
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000502
    multivalued: false
    alias: mean_peak_frict_vel
    owner: Water
    domain_of:
    - MicrobialMatBiofilm
    - Sediment
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  misc_param:
    name: misc_param
    description: Any other measurement performed or parameter collected, that is not
      listed here
    title: miscellaneous parameter
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    string_serialization: '{text};{float} {unit}'
    slot_uri: MIXS:0000752
    multivalued: true
    alias: misc_param
    owner: Water
    domain_of:
    - Agriculture
    - Air
    - FoodAnimalAndAnimalFeed
    - FoodFarmEnvironment
    - FoodFoodProductionFacility
    - FoodHumanFoods
    - HostAssociated
    - HumanAssociated
    - HumanGut
    - HumanOral
    - HumanSkin
    - HumanVaginal
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - PlantAssociated
    - Sediment
    - Soil
    - SymbiontAssociated
    - WastewaterSludge
    - Water
    range: string
    required: false
    recommended: false
  n_alkanes:
    name: n_alkanes
    description: Concentration of n-alkanes; can include multiple n-alkanes
    title: n-alkanes
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    string_serialization: '{text};{float} {unit}'
    slot_uri: MIXS:0000503
    multivalued: true
    alias: n_alkanes
    owner: Water
    domain_of:
    - MicrobialMatBiofilm
    - Sediment
    - Water
    range: string
    required: false
    recommended: false
  nitrate:
    name: nitrate
    description: Concentration of nitrate in the sample
    title: nitrate
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000425
    multivalued: false
    alias: nitrate
    owner: Water
    domain_of:
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - WastewaterSludge
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  nitrite:
    name: nitrite
    description: Concentration of nitrite in the sample
    title: nitrite
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000426
    multivalued: false
    alias: nitrite
    owner: Water
    domain_of:
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  nitro:
    name: nitro
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: micromole per liter
    description: Concentration of nitrogen (total)
    title: nitrogen
    notes:
    - nitrogen
    examples:
    - value: 4.2 micromole per liter
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000504
    multivalued: false
    alias: nitro
    owner: Water
    domain_of:
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  org_carb:
    name: org_carb
    description: Concentration of organic carbon
    title: organic carbon
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000508
    multivalued: false
    alias: org_carb
    owner: Water
    domain_of:
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  org_matter:
    name: org_matter
    description: Concentration of organic matter
    title: organic matter
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000204
    multivalued: false
    alias: org_matter
    owner: Water
    domain_of:
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Soil
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  org_nitro:
    name: org_nitro
    description: Concentration of organic nitrogen
    title: organic nitrogen
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000205
    multivalued: false
    alias: org_nitro
    owner: Water
    domain_of:
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Soil
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  organism_count:
    name: organism_count
    description: 'Total cell count of any organism (or group of organisms) per gram,
      volume or area of sample, should include name of organism followed by count.
      The method that was used for the enumeration (e.g. qPCR, atp, mpn, etc.) Should
      also be provided. (example: total prokaryotes; 3.5e7 cells per ml; qpcr)'
    title: organism count
    examples:
    - value: total prokaryotes;3.5e7 cells per milliliter;qPCR
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    string_serialization: '{text};{float} {unit};[qPCR|ATP|MPN|other]'
    slot_uri: MIXS:0000103
    multivalued: true
    alias: organism_count
    owner: Water
    domain_of:
    - Agriculture
    - Air
    - BuiltEnvironment
    - FoodAnimalAndAnimalFeed
    - FoodFarmEnvironment
    - FoodFoodProductionFacility
    - FoodHumanFoods
    - HostAssociated
    - HumanAssociated
    - HumanGut
    - HumanOral
    - HumanSkin
    - HumanVaginal
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - PlantAssociated
    - Sediment
    - SymbiontAssociated
    - WastewaterSludge
    - Water
    range: string
    required: false
    recommended: false
  oxy_stat_samp:
    name: oxy_stat_samp
    description: Oxygenation status of sample
    title: oxygenation status of sample
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000753
    multivalued: false
    alias: oxy_stat_samp
    owner: Water
    domain_of:
    - Agriculture
    - Air
    - HostAssociated
    - HumanAssociated
    - HumanGut
    - HumanOral
    - HumanSkin
    - HumanVaginal
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - PlantAssociated
    - Sediment
    - SymbiontAssociated
    - WastewaterSludge
    - Water
    range: OXY_STAT_SAMP_ENUM
    required: false
    recommended: false
  ph:
    name: ph
    description: Ph measurement of the sample, or liquid portion of sample, or aqueous
      phase of the fluid
    title: pH
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0001001
    multivalued: false
    alias: ph
    owner: Water
    domain_of:
    - FoodFarmEnvironment
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Soil
    - WastewaterSludge
    - Water
    range: float
    required: false
    recommended: false
  part_org_carb:
    name: part_org_carb
    description: Concentration of particulate organic carbon
    title: particulate organic carbon
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000515
    multivalued: false
    alias: part_org_carb
    owner: Water
    domain_of:
    - MicrobialMatBiofilm
    - Sediment
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  part_org_nitro:
    name: part_org_nitro
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: microgram per liter, micromole per liter
    description: Concentration of particulate organic nitrogen
    title: particulate organic nitrogen
    notes:
    - nitrogen
    - organic
    - particle
    - particulate
    examples:
    - value: 0.3 micromole per liter
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000719
    multivalued: false
    alias: part_org_nitro
    owner: Water
    domain_of:
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  perturbation:
    name: perturbation
    description: Type of perturbation, e.g. chemical administration, physical disturbance,
      etc., coupled with perturbation regimen including how many times the perturbation
      was repeated, how long each perturbation lasted, and the start and end time
      of the entire perturbation period; can include multiple perturbation types
    title: perturbation
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    string_serialization: '{text};{Rn/start_time/end_time/duration}'
    slot_uri: MIXS:0000754
    multivalued: true
    alias: perturbation
    owner: Water
    domain_of:
    - Agriculture
    - Air
    - FoodAnimalAndAnimalFeed
    - FoodFarmEnvironment
    - FoodHumanFoods
    - HostAssociated
    - HumanAssociated
    - HumanGut
    - HumanOral
    - HumanSkin
    - HumanVaginal
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - PlantAssociated
    - Sediment
    - SymbiontAssociated
    - WastewaterSludge
    - Water
    range: string
    required: false
    recommended: false
  petroleum_hydrocarb:
    name: petroleum_hydrocarb
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: micromole per liter
    description: Concentration of petroleum hydrocarbon
    title: petroleum hydrocarbon
    notes:
    - hydrocarbon
    - petroleum
    examples:
    - value: 0.05 micromole per liter
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000516
    multivalued: false
    alias: petroleum_hydrocarb
    owner: Water
    domain_of:
    - MicrobialMatBiofilm
    - Sediment
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  phaeopigments:
    name: phaeopigments
    annotations:
      Expected_value:
        tag: Expected_value
        value: phaeopigment name;measurement value
      Preferred_unit:
        tag: Preferred_unit
        value: milligram per cubic meter
    description: Concentration of phaeopigments; can include multiple phaeopigments
    title: phaeopigments
    examples:
    - value: 2.5 milligram per cubic meter
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    string_serialization: '{text};{float} {unit}'
    slot_uri: MIXS:0000180
    multivalued: true
    alias: phaeopigments
    owner: Water
    domain_of:
    - MicrobialMatBiofilm
    - Sediment
    - Water
    range: string
    required: false
    recommended: false
  phosphate:
    name: phosphate
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: micromole per liter
    description: Concentration of phosphate
    title: phosphate
    notes:
    - phosphate
    examples:
    - value: 0.7 micromole per liter
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000505
    multivalued: false
    alias: phosphate
    owner: Water
    domain_of:
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - WastewaterSludge
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  phosplipid_fatt_acid:
    name: phosplipid_fatt_acid
    description: Concentration of phospholipid fatty acids; can include multiple values
    title: phospholipid fatty acid
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    string_serialization: '{text};{float} {unit}'
    slot_uri: MIXS:0000181
    multivalued: true
    alias: phosplipid_fatt_acid
    owner: Water
    domain_of:
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Water
    range: string
    required: false
    recommended: false
  photon_flux:
    name: photon_flux
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: number of photons per second per unit area
    description: Measurement of photon flux
    title: photon flux
    examples:
    - value: 3.926 micromole photons per second per square meter
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000725
    multivalued: false
    alias: photon_flux
    owner: Water
    domain_of:
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  potassium:
    name: potassium
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: milligram per liter, parts per million
    description: Concentration of potassium in the sample
    title: potassium
    examples:
    - value: 463 milligram per liter
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000430
    multivalued: false
    alias: potassium
    owner: Water
    domain_of:
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  pressure:
    name: pressure
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: atmosphere
    description: Pressure to which the sample is subject to, in atmospheres
    title: pressure
    notes:
    - pressure
    examples:
    - value: 50 atmosphere
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000412
    multivalued: false
    alias: pressure
    owner: Water
    domain_of:
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  primary_prod:
    name: primary_prod
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: milligram per cubic meter per day, gram per square meter per day
    description: Measurement of primary production, generally measured as isotope
      uptake
    title: primary production
    notes:
    - primary
    - production
    examples:
    - value: 100 milligram per cubic meter per day
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000728
    multivalued: false
    alias: primary_prod
    owner: Water
    domain_of:
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  redox_potential:
    name: redox_potential
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: millivolt
    description: Redox potential, measured relative to a hydrogen cell, indicating
      oxidation or reduction potential
    title: redox potential
    examples:
    - value: 300 millivolt
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000182
    multivalued: false
    alias: redox_potential
    owner: Water
    domain_of:
    - MicrobialMatBiofilm
    - Sediment
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  salinity:
    name: salinity
    description: The total concentration of all dissolved salts in a liquid or solid
      sample. While salinity can be measured by a complete chemical analysis, this
      method is difficult and time consuming. More often, it is instead derived from
      the conductivity measurement. This is known as practical salinity. These derivations
      compare the specific conductance of the sample to a salinity standard such as
      seawater
    title: salinity
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000183
    multivalued: false
    alias: salinity
    owner: Water
    domain_of:
    - Air
    - FoodFarmEnvironment
    - HostAssociated
    - HumanAssociated
    - HumanGut
    - HumanOral
    - HumanSkin
    - HumanVaginal
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - PlantAssociated
    - Sediment
    - SymbiontAssociated
    - WastewaterSludge
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  samp_store_dur:
    name: samp_store_dur
    description: Duration for which the sample was stored
    title: sample storage duration
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    string_serialization: '{duration}'
    slot_uri: MIXS:0000116
    multivalued: false
    alias: samp_store_dur
    owner: Water
    domain_of:
    - Agriculture
    - Air
    - FoodAnimalAndAnimalFeed
    - FoodFarmEnvironment
    - FoodFoodProductionFacility
    - FoodHumanFoods
    - HostAssociated
    - HumanAssociated
    - HumanGut
    - HumanOral
    - HumanSkin
    - HumanVaginal
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - PlantAssociated
    - Sediment
    - SymbiontAssociated
    - WastewaterSludge
    - Water
    range: string
    required: false
    recommended: false
  samp_store_loc:
    name: samp_store_loc
    description: Location at which sample was stored, usually name of a specific freezer/room
    title: sample storage location
    examples:
    - value: Freezer no:5
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000755
    multivalued: false
    alias: samp_store_loc
    owner: Water
    domain_of:
    - Agriculture
    - Air
    - FoodAnimalAndAnimalFeed
    - FoodFoodProductionFacility
    - FoodHumanFoods
    - HostAssociated
    - HumanAssociated
    - HumanGut
    - HumanOral
    - HumanSkin
    - HumanVaginal
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - PlantAssociated
    - Sediment
    - SymbiontAssociated
    - WastewaterSludge
    - Water
    range: string
    required: false
    recommended: false
  samp_store_temp:
    name: samp_store_temp
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: degree Celsius
    description: Temperature at which sample was stored, e.g. -80 degree Celsius
    title: sample storage temperature
    notes:
    - sample
    - storage
    - temperature
    examples:
    - value: -80 degree Celsius
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000110
    multivalued: false
    alias: samp_store_temp
    owner: Water
    domain_of:
    - Agriculture
    - Air
    - FoodAnimalAndAnimalFeed
    - FoodFarmEnvironment
    - FoodFoodProductionFacility
    - FoodHumanFoods
    - HostAssociated
    - HumanAssociated
    - HumanGut
    - HumanOral
    - HumanSkin
    - HumanVaginal
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - PlantAssociated
    - Sediment
    - SymbiontAssociated
    - WastewaterSludge
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  samp_vol_we_dna_ext:
    name: samp_vol_we_dna_ext
    description: 'Volume (ml) or mass (g) of total collected sample processed for
      DNA extraction. Note: total sample collected should be entered under the term
      Sample Size (MIXS:0000001).'
    title: sample volume or weight for DNA extraction
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000111
    multivalued: false
    alias: samp_vol_we_dna_ext
    owner: Water
    domain_of:
    - Agriculture
    - Air
    - FoodAnimalAndAnimalFeed
    - FoodFarmEnvironment
    - FoodFoodProductionFacility
    - FoodHumanFoods
    - HostAssociated
    - HumanAssociated
    - HumanGut
    - HumanOral
    - HumanSkin
    - HumanVaginal
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MigsBa
    - MigsEu
    - MigsOrg
    - MigsPl
    - MigsVi
    - Mimag
    - MimarksC
    - MimarksS
    - Mims
    - Misag
    - MiscellaneousNaturalOrArtificialEnvironment
    - Miuvig
    - PlantAssociated
    - Sediment
    - Soil
    - SymbiontAssociated
    - WastewaterSludge
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  silicate:
    name: silicate
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: micromole per liter
    description: Concentration of silicate
    title: silicate
    examples:
    - value: 0.05 micromole per liter
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000184
    multivalued: false
    alias: silicate
    owner: Water
    domain_of:
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  size_frac_low:
    name: size_frac_low
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: micrometer
    description: Refers to the mesh/pore size used to pre-filter/pre-sort the sample.
      Materials larger than the size threshold are excluded from the sample
    title: size-fraction lower threshold
    notes:
    - lower
    examples:
    - value: 0.2 micrometer
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000735
    multivalued: false
    alias: size_frac_low
    owner: Water
    domain_of:
    - Agriculture
    - FoodFarmEnvironment
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  size_frac_up:
    name: size_frac_up
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: micrometer
    description: Refers to the mesh/pore size used to retain the sample. Materials
      smaller than the size threshold are excluded from the sample
    title: size-fraction upper threshold
    notes:
    - upper
    examples:
    - value: 20 micrometer
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000736
    multivalued: false
    alias: size_frac_up
    owner: Water
    domain_of:
    - Agriculture
    - FoodFarmEnvironment
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  sodium:
    name: sodium
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: milligram per liter, parts per million
    description: Sodium concentration in the sample
    title: sodium
    examples:
    - value: 10.5 milligram per liter
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000428
    multivalued: false
    alias: sodium
    owner: Water
    domain_of:
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - WastewaterSludge
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  soluble_react_phosp:
    name: soluble_react_phosp
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: micromole per liter, milligram per liter, parts per million
    description: Concentration of soluble reactive phosphorus
    title: soluble reactive phosphorus
    notes:
    - phosphorus
    - soluble
    examples:
    - value: 0.1 milligram per liter
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000738
    multivalued: false
    alias: soluble_react_phosp
    owner: Water
    domain_of:
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  sulfate:
    name: sulfate
    description: Concentration of sulfate in the sample
    title: sulfate
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000423
    multivalued: false
    alias: sulfate
    owner: Water
    domain_of:
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  sulfide:
    name: sulfide
    description: Concentration of sulfide in the sample
    title: sulfide
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000424
    multivalued: false
    alias: sulfide
    owner: Water
    domain_of:
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MiscellaneousNaturalOrArtificialEnvironment
    - Sediment
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  suspend_part_matter:
    name: suspend_part_matter
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: milligram per liter
    description: Concentration of suspended particulate matter
    title: suspended particulate matter
    notes:
    - particle
    - particulate
    - suspended
    examples:
    - value: 0.5 milligram per liter
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000741
    multivalued: false
    alias: suspend_part_matter
    owner: Water
    domain_of:
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  temp:
    name: temp
    description: Temperature of the sample at the time of sampling
    title: temperature
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000113
    multivalued: false
    alias: temp
    owner: Water
    domain_of:
    - Agriculture
    - Air
    - FoodAnimalAndAnimalFeed
    - FoodFarmEnvironment
    - FoodHumanFoods
    - HostAssociated
    - HumanAssociated
    - HumanGut
    - HumanOral
    - HumanSkin
    - HumanVaginal
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - MicrobialMatBiofilm
    - MigsBa
    - MigsEu
    - MigsOrg
    - MigsPl
    - MigsVi
    - Mimag
    - MimarksC
    - MimarksS
    - Mims
    - Misag
    - MiscellaneousNaturalOrArtificialEnvironment
    - Miuvig
    - PlantAssociated
    - Sediment
    - Soil
    - SymbiontAssociated
    - WastewaterSludge
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  tidal_stage:
    name: tidal_stage
    description: Stage of tide
    title: tidal stage
    examples:
    - value: high tide
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000750
    multivalued: false
    alias: tidal_stage
    owner: Water
    domain_of:
    - Sediment
    - Water
    range: TIDAL_STAGE_ENUM
    required: false
    recommended: false
  tot_depth_water_col:
    name: tot_depth_water_col
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: meter
    description: Measurement of total depth of water column
    title: total depth of water column
    notes:
    - depth
    - total
    - water
    examples:
    - value: 500 meter
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000634
    multivalued: false
    alias: tot_depth_water_col
    owner: Water
    domain_of:
    - Sediment
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  tot_diss_nitro:
    name: tot_diss_nitro
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: microgram per liter
    description: 'Total dissolved nitrogen concentration, reported as nitrogen, measured
      by: total dissolved nitrogen = NH4 + NO3NO2 + dissolved organic nitrogen'
    title: total dissolved nitrogen
    notes:
    - dissolved
    - nitrogen
    - total
    examples:
    - value: 40 microgram per liter
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000744
    multivalued: false
    alias: tot_diss_nitro
    owner: Water
    domain_of:
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  tot_inorg_nitro:
    name: tot_inorg_nitro
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: microgram per liter
    description: Total inorganic nitrogen content
    title: total inorganic nitrogen
    notes:
    - inorganic
    - nitrogen
    - total
    examples:
    - value: 40 microgram per liter
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000745
    multivalued: false
    alias: tot_inorg_nitro
    owner: Water
    domain_of:
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  tot_nitro:
    name: tot_nitro
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: microgram per liter, micromole per liter, milligram per liter
    description: 'Total nitrogen concentration of water samples, calculated by: total
      nitrogen = total dissolved nitrogen + particulate nitrogen. Can also be measured
      without filtering, reported as nitrogen'
    title: total nitrogen concentration
    notes:
    - concentration
    - nitrogen
    - total
    examples:
    - value: 50 micromole per liter
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000102
    multivalued: false
    alias: tot_nitro
    owner: Water
    domain_of:
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - WastewaterSludge
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  tot_part_carb:
    name: tot_part_carb
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: microgram per liter, micromole per liter
    description: Total particulate carbon content
    title: total particulate carbon
    notes:
    - carbon
    - particle
    - particulate
    - total
    examples:
    - value: 35 micromole per liter
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000747
    multivalued: false
    alias: tot_part_carb
    owner: Water
    domain_of:
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  tot_phosp:
    name: tot_phosp
    description: 'Total phosphorus concentration in the sample, calculated by: total
      phosphorus = total dissolved phosphorus + particulate phosphorus'
    title: total phosphorus
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000117
    multivalued: false
    alias: tot_phosp
    owner: Water
    domain_of:
    - Agriculture
    - HydrocarbonResourcesCores
    - HydrocarbonResourcesFluidsSwabs
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  turbidity:
    name: turbidity
    description: Measure of the amount of cloudiness or haziness in water caused by
      individual particles
    title: turbidity
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000191
    multivalued: false
    alias: turbidity
    owner: Water
    domain_of:
    - FoodFarmEnvironment
    - MicrobialMatBiofilm
    - Sediment
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$
  water_current:
    name: water_current
    annotations:
      Preferred_unit:
        tag: Preferred_unit
        value: cubic meter per second, knots
    description: Measurement of magnitude and direction of flow within a fluid
    title: water current
    notes:
    - water
    examples:
    - value: 10 cubic meter per second
    from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
    rank: 1000
    slot_uri: MIXS:0000203
    multivalued: false
    alias: water_current
    owner: Water
    domain_of:
    - MiscellaneousNaturalOrArtificialEnvironment
    - Water
    range: string
    required: false
    recommended: false
    pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>