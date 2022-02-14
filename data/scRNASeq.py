import os
from torch.utils.data import Dataset
import pandas as pd

class scRNASeq(Dataset):
    def __init__(
            self,
            scRNASeq_dir,
            data_type="train",
            cell_type=None,
    ):
        self.scRNASeq_dir=scRNASeq_dir
        self.data_type=data_type
        self.cell_type=cell_type
        self.cell_types=["Veinous", "T cell", "SMC", "Pericyte", "Capillary", "Arterial", "Oligo", "P. Fibro", "Ependymal", "Microglia","Astrocyte", "OPC", "M. Fibro", "Neuron"]

        self.files = os.listdir(os.path.join(self.scRNASeq_dir,self.data_type))
        print(self.files)
        self.AD_files_name=[name for name in self.files if name[:2] == "AD" and self.cell_type in name]
        self.Control_files_name=[name for name in self.files if name[:1] == "C" and self.cell_type in name]

        self.AD_cell_type_files = [os.path.join(self.scRNASeq_dir,self.data_type,ad_file) for ad_file in self.AD_files_name if cell_type in ad_file]
        self.Control_cell_type_files = [os.path.join(self.scRNASeq_dir,self.data_type,contro_file) for contro_file in self.Control_files_name if cell_type in contro_file]

    def load_data(self):
        assert self.cell_type in self.cell_types,print("The cell type(%s) is invalid." % self.cell_type)
        features = []
        tags = []

        # Loading the AD data, the label is set to 1.
        for ad_file in self.AD_cell_type_files:
            df = pd.read_csv(ad_file, header=None, low_memory=False)
            df = df.loc[1:, :]
            first_column = df.columns[0]
            df = df.drop([first_column], axis=1)
            for index, row in df.iterrows():
                features.append(row.tolist())
                tags.append(1)

        # Loading the Control data，the label is set to 0.
        for control_file in self.Control_cell_type_files:
            df = pd.read_csv(control_file, header=None, low_memory=False)
            df = df.loc[1:,:]
            first_column = df.columns[0]
            df = df.drop([first_column], axis=1)

            for index, row in df.iterrows():
                features.append(row.tolist())
                tags.append(0)

        return features, tags

