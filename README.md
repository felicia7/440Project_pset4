# 440Project_pset4
 This repo contains code and data for the first PCA attempt with
 the activated peripheral blood mononuclear cells (PBMCs)
 This paper/data can be accessed here: https://www.sciencedirect.com/science/article/pii/S1874391912005428#ec0005
 HOWEVER, the supplemental table 2 (used in this analysis)
 is only downloadable as a PDF from the publisher and
 requires extensive clean up to be used.
 For this reason the original data table is located
 in this repo titled "activated_PBMC.xlsx"

 The code used for PCA analysis is similar to the above
 but columns not needed for this initial analysis were removed,
 this file is titled "activated_PBMC_trimmed.xlsx"

 Data used is group by activated PBMCs and untreated groups,
 along with whether the proteins identified are from nuclear,
 cytoplasm, or secreted fractions.
  Activated cells were treated with lipopolysaccaride (LPS)
  which induces an immune response in monocytes
  via a toll-like pathway.

  Analysis code is written in python and requires pandas, sklearn.preprocessing,
  sklearn.decomposition (for PCA), and matplotlib
