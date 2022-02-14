import torch.nn as nn
import torch

class TransformerEncoderModel(torch.nn.Module):
    def __init__(self, gene_num):
        super(TransformerEncoderModel, self).__init__()
        self.gene_num=gene_num
        self.d_model=512
        self.linear_trans_1 = torch.nn.Linear(self.gene_num, self.d_model,bias=False)
        self.transformer_encoder_layer = nn.TransformerEncoder(nn.TransformerEncoderLayer(d_model=self.d_model, nhead=8, activation='gelu', dropout=0.8), num_layers=3)

        self.linear_output_1 = torch.nn.Linear(self.d_model, 2, bias=False)

        self.logsoftmax = torch.nn.LogSoftmax(dim=-1)
        self.softmax=torch.nn.Softmax(dim=-1)

    def forward(self, x):
        x = self.linear_trans_1(x)

        x = self.transformer_encoder_layer(x)

        output=self.linear_output_1(x)

        output=torch.squeeze(output.transpose(0, 1))
        output = self.logsoftmax(output)

        return output

    def predict(self, x):
        x = self.linear_trans_1(x)

        x = self.transformer_encoder_layer(x)

        output=self.linear_output_1(x)

        output=torch.squeeze(output.transpose(0, 1))

        return output
        
    def predict_metric(self, x):
        x = self.linear_trans_1(x)

        x = self.transformer_encoder_layer(x)

        output=self.linear_output_1(x)

        output=torch.squeeze(output.transpose(0, 1))
        output=self.softmax(output)

        return output
