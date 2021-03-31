# 440Project_pset4
 This repo contains code and data for the first PCA attempt with
 the activated peripheral blood mononuclear cells (PBMCs)
 This paper/data can be accessed here: https://www.sciencedirect.com/science/article/pii/S1874391912005428#ec0005
 HOWEVER, the supplemental table 2 (used in this analysis)
 is only downloadable as a PDF from the publisher and
 requires extensive clean up to be used.
 For this reason the original data table is located
 in this repo titled "activated_PBMC.xlsx" for reference

Code analysis:
 The data file used for PCA analysis is similar to the above
 but columns not needed for this initial analysis were removed,
 this file is titled "activated_PBMC_trimmed.xlsx"
 Protein abundance values are estimated using the exponentially modified
  protein abundance index (emPAI).
  PCA was used to cluster emPAI scores by whether
  the protein was identified in activated, untreated, or both samples. 

 Folder Structure:
Within 440Project_pset4 there is an analysis folder and a 'Project_data' folder. The code required for PCA analysis along with a subfolder where figures are stored are located in the analysis folder. Project_data folder is where the excel files used are located and the code calls from a relative path so this shouldn't need to be changed unless folder structure is changed.

Data details:
 Data used is group by activated PBMCs and untreated groups,
 along with whether the proteins identified are from nuclear,
 cytoplasm, or secreted fractions.
  Activated cells were treated with lipopolysaccaride (LPS)
  which induces an immune response in monocytes
  via a toll-like pathway.

Python requirements:
  Analysis code is written in python and requires pandas, sklearn.preprocessing,
  sklearn.decomposition (for PCA), and matplotlib
