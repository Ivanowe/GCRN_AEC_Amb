import torch
import numpy as np

class LossFunction(object):
    #old version kept for reference
    def __call__(self, est, lbl, loss_mask, n_frames):
        est *= loss_mask
        lbl *= loss_mask

        n_feats = est.shape[-1]

        loss = torch.sum((est - lbl)**2) / float(sum(n_frames) * n_feats * 2)
        
        return loss