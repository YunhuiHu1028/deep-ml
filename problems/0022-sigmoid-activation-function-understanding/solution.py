import torch

def sigmoid(z: float) -> float:
    """
    Compute the sigmoid activation function.
    Input:
      - z: float or torch scalar tensor
    Returns:
      - sigmoid(z) as Python float rounded to 4 decimals.
    """
    # Your implementation here
    z_tensor = torch.as_tensor(z, dtype=torch.float32)
    result = 1/(1 + torch.exp(-z_tensor))
    return round(result.item(), 4)
