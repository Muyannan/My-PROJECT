import torch
indices=torch.tensor([[1,2],[3,4]])
indices2=torch.tensor([[0,1],[0,2]])
b=indices[None, :, :] - indices2[:, None, :] 

b=indices[None, :, :] - indices2[:, :, None]  

indices=torch.tensor([1,2])
a=indices[None,:]-torch.tensor([[0,1],[0,2]])
print(a)  

indices=torch.tensor([1,2])
a=indices[:,None]-torch.tensor([[0,1],[0,2]])
print(a)  
print(b)