import argparse
import os
import torch
import experiment 

def train_epoch(model, dataloader, criterion, optimizer, device):
    model.train()
    running_loss, correct, total = 0.0, 0, 0

    for inputs, targets in dataloader:
        inputs, targets = inputs.to(device), targets.to(device)
        
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()

        running_loss += loss.item() * inputs.size(0)
        _, predicted = outputs.max(1)
        total += targets.size(0)
        correct += predicted.eq(targets).sum().item()

    return running_loss / total, correct / total

def validation_epoch(model, dataloader, criterion, device):
    model.eval()
    running_loss, correct, total = 0.0, 0, 0

    with torch.no_grad():
        for inputs, targets in dataloader:
            inputs, targets = inputs.to(device), targets.to(device)
            outputs = model(inputs)
            loss = criterion(outputs, targets)

            running_loss += loss.item() * inputs.size(0)
            _, predicted = outputs.max(1)
            total += targets.size(0)
            correct += predicted.eq(targets).sum().item()

    return running_loss / total, correct / total

def main():
    parser = argparse.ArgumentParser()
    
    max_workers = os.cpu_count() or 1
    parser.add_argument('--num_workers', type=int, default=max_workers,
                        help=f'Number of data loader workers (default: {max_workers})')
    parser.add_argument('--num_epochs', type=int, default=5,
                        help='Number of epochs to train (default: 5)')
    
    device_group = parser.add_mutually_exclusive_group()
    device_group.add_argument('--cpu', action='store_true', help='Force training on CPU')
    device_group.add_argument('--gpu', action='store_true', help='Force training on GPU')

    args = parser.parse_args()

    if args.cpu:
        device = torch.device("cpu")
    elif args.gpu:
        if torch.cuda.is_available():
            device = torch.device("cuda")
        else:
            print("Warning: GPU requested but CUDA is not available. Falling back to CPU.")
            device = torch.device("cpu")
    else:
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    print(f"Running on device: {device}")
    print(f"Using {args.num_workers} worker(s) for data loading.")

    print("Loading data and model from local experiment.py...")
    train_loader, validation_loader = experiment.get_dataloaders(args.num_workers)
    model = experiment.get_model().to(device)
    criterion = experiment.get_criterion()
    optimizer = experiment.get_optimizer(model)

    history = {'train_loss': [], 'validation_loss': [], 'train_acc': [], 'validation_acc': []}

    print("Starting training...")
    for epoch in range(1, args.num_epochs + 1):
        tr_loss, tr_acc = train_epoch(model, train_loader, criterion, optimizer, device)
        va_loss, va_acc = validation_epoch(model, validation_loader, criterion, device)
        
        history['train_loss'].append(tr_loss)
        history['train_acc'].append(tr_acc)
        history['validation_loss'].append(va_loss)
        history['validation_acc'].append(va_acc)
        
        print(f"Epoch [{epoch}/{args.num_epochs}] - "
              f"Train Loss: {tr_loss:.4f}, Train Acc: {tr_acc:.4f} | "
              f"Validation Loss: {va_loss:.4f}, Validation Acc: {va_acc:.4f}")

    experiment.plot_metrics(history)

if __name__ == '__main__':
    main()