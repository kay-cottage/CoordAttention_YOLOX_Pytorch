import torch
state_dict = torch.load('model_data/yolox_s.pth')
torch.save(state_dict, 'yolox_s.pth', _use_new_zipfile_serialization=False)
