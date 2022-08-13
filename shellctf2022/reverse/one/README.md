# INSTALL

```docker pull qilingframework/qiling:latest```

Also need to update rootfs:

```
docker run -dt --name qiling  qilingframework/qiling:latest
docker exec -it qiling /bin/bash
cd /qiling
git submodule update --init --recursive
```

