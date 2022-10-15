# !pip install nptyping
import numpy as np
from typing import List, Tuple

from nptyping import NDArray
import torch
import torch.nn as nn


def generate_tensor(data: List[List[List]], size: int = 32) -> torch.Tensor:
    """生データから画像データのテンソル

    """
    return torch.Tensor([
        [
            [
                [
                    d[1] for _ in range(size)
                ],
                [
                    d[2] for _ in range(size)
                ],
                [
                    d[3] for _ in range(size)
                ],
            ]
        ] for d in data
    ])


class VitIiputLayer(nn.Module):
    def __init__(
        self,
        in_channels: int = 3,
        emb_dim: int = 384,
        num_patch_row: int = 2,
        image_size: int = 32
    ):
        super().__init__()
        self.in_channels = in_channels
        self.emb_dim = emb_dim
        self.num_patch_row = num_patch_row
        self.image_size = image_size

        # パッチ数
        self.num_patch = num_patch_row ** 2

        # パッチの大きさ
        self.patch_size = int(self.image_size // self.num_patch_row)

        # パッチへの分割
        self.patch_emb_layer = nn.Conv2d(
            in_channels=self.in_channels,
            out_channels=self.emb_dim,
            kernel_size=self.patch_size,
            stride=self.patch_size
        )

        # CLS Token
        self.cls_token = nn.parameter.Parameter(
            torch.randn(1, 1, emb_dim)
        )

        # Position Embedded
        self.pos_emb = nn.parameter.Parameter(
            torch.randn(1, self.num_patch + 1, emb_dim)
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        z_0 = self.patch_emb_layer(x)

        z_0 = z_0.flatten(2)
        z_0 = z_0.transpose(1, 2)

        z_0 = torch.cat(
            [self.cls_token.repeat(repeats=(x.size(0), 1, 1)), z_0],
            dim=1
        )

        z_0 = z_0 + self.pos_emb

        return z_0


if __name__ == '__main__':
