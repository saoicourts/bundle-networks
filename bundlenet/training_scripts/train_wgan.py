import torch
import argparse

from bundlenet import WGAN_div

parser = argparse.ArgumentParser(description='Train a WGAN.')
parser.add_argument('--epochs', default=2000, type=int)
parser.add_argument('--batch_size', default=100, type=int)
parser.add_argument('--lr', default=1e-4, type=float)
parser.add_argument('--latent_dim', default=10, type=int)
parser.add_argument('--device', default='cpu')
parser.add_argument('--wt_dir', default='WGAN_sliced_torus')
parser.add_argument('--n_critic', default=5)
args = parser.parse_args()

base_points = torch.load('../../datasets/sliced_torus_base.pt')
bundle_points = torch.load('../../datasets/sliced_torus_bundle.pt')
    
model = WGAN_div(bundle_points, base_points,
            device=args.device,
            latent_dim=args.latent_dim
        )

model.train_net(
        lr=args.lr,
        num_epochs=args.epochs,
        batch_size=args.batch_size,
        save_weights=True,
        wt_dir='../../saved_weights/' + args.wt_dir,
        n_critic=args.n_critic
    )
