# When a helpful intention leads to an unsafe choice

**Paper:** [Users Really Do Plug in USB Drives They Find](https://doi.org/10.1109/SP.2016.26) ([author-hosted PDF](https://faculty.cc.gatech.edu/~mbailey/publications/oakland16_usb.pdf))  
**Authors:** Matthew Tischer, Zakir Durumeric, Sam Foster, Sunny Duan, Alec Mori, Elie Bursztein and Michael Bailey  
**Published:** IEEE Symposium on Security and Privacy, 2016, pp. 306–319  
**Access:** FULL TEXT APPRAISED on 12 October 2026  
**Note:** Prepared from the original paper; not a claim that the repository owner personally read or endorsed it.

## Study and comparison

In April 2015, the researchers placed 297 USB drives around a university campus, varying their appearance, location and placement time. They observed whether the drives disappeared and whether files were opened, and invited people who interacted with the drives to complete a survey about their motivations and security practices. A separate university sample provided baseline survey responses. The authors obtained ethics approval and used non-harmful study materials. See §III, pp. 2–4.

The study compared five drive appearances, including an unlabeled reference condition. The survey involved 62 valid responses from the field study and 31 from the separate baseline sample. These were not repeated measures of the same participants. See §III.C and §V, pp. 3, 6–8.

## What the authors found

The study recorded file openings for 135 of 297 drives (45%) and removal of 290 drives (98%). The reported 45–98% range is a lower-to-upper bound on possible connection behavior, **not a measured rate of successful malware execution or compromise**. A missing drive could have been taken without being connected, and a connected drive might not have generated an observable file-opening event. Median time to observed file opening was 6.9 hours. See §IV, pp. 4–5.

The more intriguing labels did not produce a significant increase in recorded file openings. The return-address condition had fewer recorded openings than the unlabeled condition (17/59 versus 27/60), but the paper reports p = 0.10, so this is not a conventional p < 0.05 finding. See §IV.A, Table I, p. 5.

Among the 62 valid survey respondents, 42 (68%) described returning the drive as their main reason for acting and 11 (18%) mentioned curiosity. These are self-reports from a selected subset, not measured motives for every person exposed to the study. See §V.A, Table V, pp. 6–7.

## Eight-domain appraisal

| Domain | Judgment | Evidence |
| --- | --- | --- |
| Design | Partial | Field conditions varied, but not all interactions were directly observed (§III–IV). |
| Sampling | Partial | Single campus; unknown total number of individual finders (§III). |
| Outcomes | Partial | Removal, file opening and actual harm are different events (§IV). |
| Confounding | Partial | Return-label placement was concentrated on one day; campus warnings circulated (§IV.A; §VI). |
| Measurement | Partial | File-opening records miss some possible interactions (§III.B; §IV). |
| Analysis | Partial | Tests and counts reported, but survey groups were small and some scale reliability was low (§IV; §V.D). |
| Generalization | Partial | University setting does not establish workplace or population-wide rates (§III; §VII). |
| Ethics/reproducibility | Partial | Ethics approval, participant withdrawal mechanism and non-harmful materials; independent replication materials not verified (§III.D). |

## Interpretation and open questions

**Interpretation:** An unsafe action may arise from an ordinary attempt to help rather than from a stated willingness to take security risks. But retrospective self-reports do not establish the motivation of everyone who interacted with a drive.

**Possible future tests, not completed studies:** Would making a safe way to return a found object obvious change the decision? Can a study distinguish noticing, picking up, using, and reporting an object without collapsing these actions into one susceptibility score? Would a safer response persist when the situation changes?

**Boundary:** No individual risk prediction or cross-channel generalization follows from this one field study. Replicating deceptive research requires separate ethics and safety review.
