"""
This file is part of the Verifying explainability of a deep learning tissue classifier trained on RNA-seq data project.

Verifying explainability of a deep learning tissue classifier trained on RNA-seq data project is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.


Verifying explainability of a deep learning tissue classifier trained on RNA-seq data project is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with the Verifying explainability of a deep learning tissue classifier trained on RNA-seq data project.  If not, see <http://www.gnu.org/licenses/>.
"""

map_dict = {
    0: "Adipose - Subcutaneous",
    1: "Adipose - Visceral (Omentum)",
    2: "Adrenal Gland",
    3: "Artery - Aorta",
    4: "Artery - Coronary",
    5: "Artery - Tibial",
    6: "Brain - Amygdala",
    7: "Brain - Anterior cingulate cortex (BA24)",
    8: "Brain - Caudate (basal ganglia)",
    9: "Brain - Cerebellar Hemisphere",
    10: "Brain - Cerebellum",
    11: "Brain - Cortex",
    12: "Brain - Frontal Cortex (BA9)",
    13: "Brain - Hippocampus",
    14: "Brain - Hypothalamus",
    15: "Brain - Nucleus accumbens (basal ganglia)",
    16: "Brain - Putamen (basal ganglia)",
    17: "Brain - Spinal cord (cervical c-1)",
    18: "Brain - Substantia nigra",
    19: "Breast - Mammary Tissue",
    20: "Colon - Sigmoid",
    21: "Colon - Transverse",
    22: "Esophagus - Gastroesophageal Junction",
    23: "Esophagus - Mucosa",
    24: "Esophagus - Muscularis",
    25: "Heart - Atrial Appendage",
    26: "Heart - Left Ventricle",
    27: "Kidney - Cortex",
    28: "Liver",
    29: "Lung",
    30: "Minor Salivary Gland",
    31: "Muscle - Skeletal",
    32: "Nerve - Tibial",
    33: "Ovary",
    34: "Pancreas",
    35: "Pituitary",
    36: "Prostate",
    37: "Skin - Not Sun Exposed (Suprapubic)",
    38: "Skin - Sun Exposed (Lower leg)",
    39: "Small Intestine - Terminal Ileum",
    40: "Spleen",
    41: "Stomach",
    42: "Testis",
    43: "Thyroid",
    44: "Uterus",
    45: "Vagina",
    46: "Whole Blood",

}


inv_map = {v: k for k, v in map_dict.items()}


colour_map = {
    "Adipose - Subcutaneous": "#db5f57",
    "Adipose - Visceral (Omentum)": "#db7057",
    "Adrenal Gland": "#db8157",
    "Artery - Aorta": "#db9157",
    "Artery - Coronary": "#dba257",
    "Artery - Tibial": "#dbb357",
    "Brain - Amygdala": "#dbc457",
    "Brain - Anterior cingulate cortex (BA24)": "#dbd557",
    "Brain - Caudate (basal ganglia)": "#d1db57",
    "Brain - Cerebellar Hemisphere": "#c0db57",
    "Brain - Cerebellum": "#afdb57",
    "Brain - Cortex": "#9edb57",
    "Brain - Frontal Cortex (BA9)": "#8ddb57",
    "Brain - Hippocampus": "#7cdb57",
    "Brain - Hypothalamus": "#6bdb57",
    "Brain - Nucleus accumbens (basal ganglia)": "#5adb57",
    "Brain - Putamen (basal ganglia)": "#57db64",
    "Brain - Spinal cord (cervical c-1)": "#57db75",
    "Brain - Substantia nigra": "#57db86",
    "Breast - Mammary Tissue": "#57db97",
    "Colon - Sigmoid": "#57dba8",
    "Colon - Transverse": "#57dbb9",
    "Esophagus - Gastroesophageal Junction": "#57dbca",
    "Esophagus - Mucosa": "#57dbdb",
    "Esophagus - Muscularis": "#57cbdb",
    "Heart - Atrial Appendage": "#57badb",
    "Heart - Left Ventricle": "#57a9db",
    "Kidney - Cortex": "#5798db",
    "Liver": "#5787db",
    "Lung": "#5776db",
    "Minor Salivary Gland": "#5765db",
    "Muscle - Skeletal": "#5957db",
    "Nerve - Tibial": "#6a57db",
    "Ovary": "#7b57db",
    "Pancreas": "#8c57db",
    "Pituitary": "#9d57db",
    "Prostate": "#ae57db",
    "Skin - Not Sun Exposed (Suprapubic)": "#bf57db",
    "Skin - Sun Exposed (Lower leg)": "#d057db",
    "Small Intestine - Terminal Ileum": "#db57d6",
    "Spleen": "#db57c5",
    "Stomach": "#db57b4",
    "Testis": "#db57a3",
    "Thyroid": "#db5792",
    "Uterus": "#db5782",
    "Vagina": "#db5771",
    "Whole Blood": "#db5760",
}

tissue_types = [
    "Adipose - Subcutaneous",
    "Muscle - Skeletal",
    "Artery - Tibial",
    "Artery - Coronary",
    "Heart - Atrial Appendage",
    "Adipose - Visceral (Omentum)",
    "Vagina",
    "Skin - Not Sun Exposed (Suprapubic)",
    "Minor Salivary Gland",
    "Brain - Cortex",
    "Adrenal Gland",
    "Thyroid",
    "Lung",
    "Spleen",
    "Pancreas",
    "Esophagus - Muscularis",
    "Esophagus - Mucosa",
    "Stomach",
    "Small Intestine - Terminal Ileum",
    "Prostate",
    "Testis",
    "Nerve - Tibial",
    "Skin - Sun Exposed (Lower leg)",
    "Heart - Left Ventricle",
    "Brain - Cerebellum",
    "Colon - Transverse",
    "Whole Blood",
    "Artery - Aorta",
    "Esophagus - Gastroesophageal Junction",
    "Colon - Sigmoid",
    "Breast - Mammary Tissue",
    "Pituitary",
    "Uterus",
    "Brain - Frontal Cortex (BA9)",
    "Brain - Caudate (basal ganglia)",
    "Brain - Nucleus accumbens (basal ganglia)",
    "Brain - Putamen (basal ganglia)",
    "Brain - Hypothalamus",
    "Brain - Spinal cord (cervical c-1)",
    "Brain - Hippocampus",
    "Brain - Anterior cingulate cortex (BA24)",
    "Ovary",
    "Brain - Cerebellar Hemisphere",
    "Liver",
    "Brain - Substantia nigra",
    "Brain - Amygdala",
    "Kidney - Cortex",
]

tissue_codes = [

    "Adipose - Sub",
    "Adipose - VO",
    "Adrenal Gland",
    "Artery - Aor",
    "Artery - Cor",
    "Artery - Tib",
    "Brain - Amy",
    "Brain - ACCB",
    "Brain - CBG",
    "Brain - CH",
    "Brain - Cer",
    "Brain - Cor",
    "Brain - FCB",
    "Brain - Hip",
    "Brain - Hyp",
    "Brain - NABG",
    "Brain - PBG",
    "Brain - SCCC",
    "Brain - SN",
    "Breast",
    "Colon - Sig",
    "Colon - Tra",
    "Esophagus - GJ",
    "Esophagus - Muc",
    "Esophagus - Mus",
    "Heart - AA",
    "Heart - LV",
    "Kidney - Cor",
    "Liver",
    "Lung",
    "Minor Salivary Gland",
    "Muscle",
    "Nerve",
    "Ovary",
    "Pancreas",
    "Pituitary",
    "Prostate",
    "Skin - NSES",
    "Skin - SELL",
    "Small Intestine",
    "Spleen",
    "Stomach",
    "Testis",
    "Thyroid",
    "Uterus",
    "Vagina",
    "Whole Blood"
]

tissue_code_map = {
    "Adipose - Subcutaneous": "Adipose - Sub",
    "Adipose - Visceral (Omentum)": "Adipose - VO",
    "Adrenal Gland": "Adrenal Gland",
    "Artery - Aorta": "Artery - Aor",
    "Artery - Coronary": "Artery - Cor",
    "Artery - Tibial": "Artery - Tib",
    "Brain - Amygdala": "Brain - Amy",
    "Brain - Anterior cingulate cortex (BA24)": "Brain - ACCB",
    "Brain - Caudate (basal ganglia)": "Brain - CBG",
    "Brain - Cerebellar Hemisphere": "Brain - CH",
    "Brain - Cerebellum": "Brain - Cer",
    "Brain - Cortex": "Brain - Cor",
    "Brain - Frontal Cortex (BA9)": "Brain - FCB",
    "Brain - Hippocampus": "Brain - Hip",
    "Brain - Hypothalamus": "Brain - Hyp",
    "Brain - Nucleus accumbens (basal ganglia)": "Brain - NABG",
    "Brain - Putamen (basal ganglia)": "Brain - PBG",
    "Brain - Spinal cord (cervical c-1)": "Brain - SCCC",
    "Brain - Substantia nigra": "Brain - SN",
    "Breast - Mammary Tissue": "Breast",
    "Colon - Sigmoid": "Colon - Sig",
    "Colon - Transverse": "Colon - Tra",
    "Esophagus - Gastroesophageal Junction": "Esophagus - GJ",
    "Esophagus - Mucosa": "Esophagus - Muc",
    "Esophagus - Muscularis": "Esophagus - Mus",
    "Heart - Atrial Appendage": "Heart - AA",
    "Heart - Left Ventricle": "Heart - LV",
    "Kidney - Cortex": "Kidney - Cor",
    "Liver": "Liver",
    "Lung": "Lung",
    "Minor Salivary Gland": "Minor Salivary Gland",
    "Muscle - Skeletal": "Muscle",
    "Nerve - Tibial": "Nerve",
    "Ovary": "Ovary",
    "Pancreas": "Pancreas",
    "Pituitary": "Pituitary",
    "Prostate": "Prostate",
    "Skin - Not Sun Exposed (Suprapubic)": "Skin - NSES",
    "Skin - Sun Exposed (Lower leg)": "Skin - SELL",
    "Small Intestine - Terminal Ileum": "Small Intestine",
    "Spleen": "Spleen",
    "Stomach": "Stomach",
    "Testis": "Testis",
    "Thyroid": "Thyroid",
    "Uterus": "Uterus",
    "Vagina": "Vagina",
    "Whole Blood": "Whole Blood",
}

colour_map_code = {
    "Adipose - Sub": "#db5f57",
    "Adipose - VO": "#db7057",
    "Adrenal Gland": "#db8157",
    "Artery - Aor": "#db9157",
    "Artery - Cor": "#dba257",
    "Artery - Tib": "#dbb357",
    "Brain - Amy": "#dbc457",
    "Brain - ACCB": "#dbd557",
    "Brain - CBG": "#d1db57",
    "Brain - CH": "#c0db57",
    "Brain - Cer": "#afdb57",
    "Brain - Cor": "#9edb57",
    "Brain - FCB": "#8ddb57",
    "Brain - Hip": "#7cdb57",
    "Brain - Hyp": "#6bdb57",
    "Brain - NABG": "#5adb57",
    "Brain - PBG": "#57db64",
    "Brain - SCCC": "#57db75",
    "Brain - SN": "#57db86",
    "Breast": "#57db97",
    "Colon - Sig": "#57dba8",
    "Colon - Tra": "#57dbb9",
    "Esophagus - GJ": "#57dbca",
    "Esophagus - Muc": "#57dbdb",
    "Esophagus - Mus": "#57cbdb",
    "Heart - AA": "#57badb",
    "Heart - LV": "#57a9db",
    "Kidney - Cor": "#5798db",
    "Liver": "#5787db",
    "Lung": "#5776db",
    "Minor Salivary Gland": "#5765db",
    "Muscle": "#5957db",
    "Nerve": "#6a57db",
    "Ovary": "#7b57db",
    "Pancreas": "#8c57db",
    "Pituitary": "#9d57db",
    "Prostate": "#ae57db",
    "Skin - NSES": "#bf57db",
    "Skin - SELL": "#d057db",
    "Small Intestine": "#db57d6",
    "Spleen": "#db57c5",
    "Stomach": "#db57b4",
    "Testis": "#db57a3",
    "Thyroid": "#db5792",
    "Uterus": "#db5782",
    "Vagina": "#db5771",
    "Whole Blood": "#db5760",
}


