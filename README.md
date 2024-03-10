# sbu-sdoh-implementation

## Assessment Tool: HRSN 
- Need to use CMS HRSN - starting with just the manditory fields, can also do aux. if want
- then need to associate with LOINC code in Cerner System: 
    - Manditory: https://loinc.org/96777-8 
    - Supplmeental: https://loinc.org/97023-6


### Flagging Assessment tool: LOINC RELATED to HRSN: 
- Currently for the fields we have: 
    - Housing: 71802-3 --> 30 
    - Food: 88122-7	--> None 
    - Food: 88123-5	 --> None 
    - Transportation: 93030-5 --> 30 
    - Utilies: 96779-4 --> None 
    - Safety (physical abuse): 95618-5 --> 10 
    - Safety (verbal abuse): 95617-7 --> 10
    - Safety (threaten physical): 95616-9 --> 10 
    - Safety (scream/curse): 95615-1	--> 10
    - Safety (total score): 95614-4	--> 10


### Flagging unmet SDoH with ICD: 
    - Across all Z55-65 codes: identified approximately 38k patients with at least one Z code at SBH.
    - Z55-Z65: Health hazards r/t socioeconomic and psychosocial circumstances: 49,030
        - Education/literarcy: Z55 ->  3340
        - Employment:  12,350 
        - Occupational risk: Z57 ->  3160
        - Physical envir: Z58 -> 20 
        - Housing/Economic: Z59 -> 7790 
        - Social environment: Z60 -> 3370 
        - Upbringing: Z62 -> 5980 
        - Other family r/t: Z63 ->  13690 
        - Psychosocial circumstances (certain): Z65 ->  4430
        - Psychosocial circumstances (other): Z65 ->  9880