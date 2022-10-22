``` mermaid 
graph LR
    image1["image1(C x H x W)"] --> patch1["patch1(C x H/P x W/P)"]
    image1 --> patch2
    image1 --> patch...
    image1 --> patchNp

    patch1 --> flatten1["flatten1(HWC/Np^2)"]
    patch2 --> flatten2
    patch... --> flatten...
    patchNp --> flattenNp

    flatten1 --> patch_emb1["patch_emb1(D)"]
    flatten2 --> patch_emb2
    flatten... --> patch_emb...
    flattenNp --> patch_embNp

    cls_token --> add_cls_token1["add_cls_token(D)"]
    patch_emb1 --> add_cls_token2
    patch_emb2 --> add_cls_token3
    patch_emb... --> add_cls_token...
    patch_embNp --> add_cls_tokenN["add_cls_tokenN(N=Np+1)"]

    pos_emb1  --> +
    pos_emb2  --> +
    pos_emb... --> +
    pos_embN  --> +
    add_cls_token1 --> +
    add_cls_token2 --> +
    add_cls_token3 --> +
    add_cls_token... --> +
    add_cls_tokenN --> +

    + --> Output

    Batch --> Patch

    subgraph Batch
        image1
        image2
        image...
        imageBn
    end

    subgraph Patch
        patch1
        patch2
        patch...
        patchNp
    end

    subgraph Flatten
        flatten1
        flatten2
        flatten...
        flattenNp
    end

    subgraph PatchEmbedded
        patch_emb1
        patch_emb2
        patch_emb...
        patch_embNp
    end

    subgraph ClassToken
        cls_token
    end

    subgraph AddClassToken
        add_cls_token1
        add_cls_token2
        add_cls_token3
        add_cls_token...
        add_cls_tokenN
    end        

    subgraph PositionEmbedded
        pos_emb1
        pos_emb2
        pos_emb...
        pos_embN
    end
```