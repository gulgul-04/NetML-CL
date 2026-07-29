import torch

def get_device():

    if torch.cuda.is_available():
        # Nvidia GPU (Windows/Linux)
        device = torch.device("cuda")
        gpu_name = torch.cuda.get_device_name(device)
        print(f"Hardware Routed: Using CUDA ({gpu_name})")
        
    elif torch.backends.mps.is_available():
        # Apple Silicon (M1/M2/M3)
        device = torch.device("mps")
        print("Hardware Routed: Using MPS (Metal Performance Shaders)")
        
    else:
        # Fallback to CPU (Intel Macs, Windows without GPU)
        device = torch.device("cpu")
        # Restrict PyTorch to use 4 threads to prevent CPU thrashing on an i5
        torch.set_num_threads(4) 
        print(f"Hardware Routed: Using CPU with {torch.get_num_threads()} threads active")
    
    return device

if __name__ == "__main__":
    device = get_device()