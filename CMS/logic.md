# Calculation using TriNetX Data 

# Denominator 
1. Check Patients 18 years and older on date of encounter:
    - Age field: >= 18 
2. Check Patient encounter during the performance period as listed in Denominator
    - Encounter date field = Somewhere between X and Y 
        - FHIR: Encounter.actualPeriod.start, Encounter.actualPeriod.end
        - https://build.fhir.org/encounter-definitions.html#Encounter.actualPeriod
        - https://build.fhir.org/datatypes.html#Period 
    - Patient encounter during the performance period (CPT): 

59400, 59510, 59610, 59618, 78012, 78070, 78075,
78102, 78140, 78185, 78195, 78202, 78215, 78261, 78290, 78300, 78305, 78315, 78414, 78428, 78456, 78458, 78579, 78580, 78582, 78597, 78601, 78630, 78699, 78708, 78725, 78740, 78801, 78803, 78999, 90791, 90792, 90832, 90834, 90837, 90839, 90845, 90945, 90947, 90951, 90952, 90953, 90954, 90955, 90956, 90957, 90958, 90959, 90960, 90961, 90962, 90963, 90964, 90965, 90966, 90967, 90968, 90969, 90970, 92002, 92004, 92012,
92014, 92507, 92508, 92521, 92522, 92523, 92524, 92526, 92537, 92538, 92540, 92541, 92542, 92544, 92545, 92548, 92549, 92550, 92557, 92567, 92568, 92570, 92588, 92625, 92626, 92650, 92651, 92652, 92653, 96116, 96156, 96158, 97129, 97161, 97162, 97163, 97164, 97802, 97803, 97804, 98960, 98961, 98962, 99203, 99204, 99205, 99211, 99212, 99213, 99214, 99215, 99221, 99222, 99223, 99231, 99232, 99233, 99236, 99242, 99243,
99244, 99245, 99281, 99282, 99283, 99284, 99285, 99304, 99305, 99306, 99307, 99308, 99309, 99310, 99381, 99382, 99383, 99384, 99385, 99386, 99387, 99391, 99392, 99393, 99394, 99395, 99396, 99397, 99401, 99402, 99403, 99404, 99411, 99412, 99429, 99495, 99496, 99512, D0120, D0140, D0145, D0150, D0160, D0170, D0180, D7111, D7140, D7210, D7220, D7230, D7240, D7241, D7250, D7251, G0101, G0108, G0270, G0271, G0402, G0438, G0439, G0447, G0473, G9054

- Need to look at 'procedures' section (code_system = CPT, var = code) of FHIR in patient, look for matching CPT codes above, and then double check the encounter code in procedures table matches 


# Numerator
1. Patients who were screened for social determinants of health (SDOH) using a standardized tool on the date of the encounter 

# Also check
1. Patients who were not screened for social determinants of health (SDOH) using a standardized tool on the date of the encounter