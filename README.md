# sbu-sdoh-implementation

## CMS

- Is very clear in instructions, screening must be performaned annually with a standardized tool.
    - Examples of standardized tools include: 
        - 1.Accountable Health Communities Health-Related Social Needs Screening Tool (2017)
        - 2.Accountable Health Communities Health-Related Social Needs Screening Tool (2021)
        - 3.The Protocol for Responding to and Assessing Patients’ Risks and Experiences (PRAPARE) Tool (2016)
        - 4.WellRx Questionnaire (2014)
        - 5.American Academy of Family Physicians (AAFP) Screening Tool (2018)

- Manditory fields from CMS measurement guide: 
    - 1.food insecurity
    - 2.housing instability
    - 3.transportation needs
    - 4.utility difficulties 
    - 5.interpersonal safety

## Assessment Tool: HRSN 
- Need to use CMS HRSN - starting with just the manditory fields, can also do aux. if want
- then need to associate with LOINC code in Cerner System
    - Manditory: https://loinc.org/96777-8 
    - Supplmeental: https://loinc.org/97023-6

## Current STATE SBH 
### Flagging Assessment tool: LOINC RELATED to HRSN 
- Based on these, it does currently appear we have ALL 5 MANDATORY fields in the system, unsure though where they are being inputted from, where they are originating from 
    - Need to research this; perhaps they are coming in from social history component section?  

- Currently for the LOINC fields we have for assessments: 
    - (1 MAND) Food: 88122-7	--> None 
    - (1 MAND) Food: 88123-5	 --> None 
    - (2 MAND) Housing: 71802-3 --> 30 
    - (3 MAND) Transportation: 93030-5 --> 30 
    - (4 MAND) Utilies: 96779-4 --> None 
    - (5 MAND) Safety (physical abuse): 95618-5 --> 10 
    - (5 MAND)Safety (verbal abuse): 95617-7 --> 10
    - (5 MAND)Safety (threaten physical): 95616-9 --> 10 
    - (5 MAND)Safety (scream/curse): 95615-1 --> 10
    - (5 MAND) Safety (total score): 95614-4 --> 10


### Flagging unmet SDoH with ICD 
- Across all Z55-65 codes: identified approximately 38k patients with at least one Z code at SBH.
- Z55-Z65: Health hazards r/t socioeconomic and psychosocial circumstances: 49,030
- For MAND1, MAND2, MAND3: have Z59 for Food, Housing, and Transportation 
- For MAND 4 + 5: UNSURE --> no clear Z-codes for these
    - Education/literarcy: Z55 ->  3340
    - Employment:  12,350 
    - Occupational risk: Z57 ->  3160
    - Physical envir: Z58 -> 20 
    - (MAND 1, MAND 2, MAND 3)Housing/Economic: Z59 -> 7790 
        - Contains FOOD + HOUSING + TRANSPORTATION
    - Social environment: Z60 -> 3370 
    - Upbringing: Z62 -> 5980 
    - Other family r/t: Z63 ->  13690 
    - Psychosocial circumstances (certain): Z65 ->  4430
    - Psychosocial circumstances (other): Z65 ->  9880

### Reltaed intevention CPT/HCPCS for 5 primary fields 
- Generic codes typically used for SDoH related: 
    - 96156	CPT - Health behavior assessment, or re-assessment (ie, health-focused clinical interview, behavioral observations, clinical decision making)	
    - 96160 CPT - Administration of patient-focused health risk assessment instrument (eg, health hazard appraisal) with scoring and documentation, per standardized instrument	
    - 96161	CPT - Administration of caregiver-focused health risk assessment instrument (eg, depression inventory) for the benefit of the patient, with scoring and documentation, per standardized instrument	

- Below is looking at https://confluence.hl7.org/display/GRAV/Social+Risk+Terminology+Value+Sets for intervention/procedures that can be documented: 
    - (1 MAND) Food Interventions: S9470, 97803, 97804 --> 7120 
    - (2 MAND) Housing Interventions: --- no specific CPT/HCPCS codes yet 
    - (3 MAND) Transportation Interventions: --- no specific CPT/HCPCS codes yet 
    - (4 MAND) Utilies Interventions: --- no specific CPT/HCPCS codes yet 
    - (5 MAND) Safety Interventions: --- no specific CPT/HCPCS codes yet 