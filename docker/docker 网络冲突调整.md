
## docker 使用指定网段

在使用docker  网段配置不当可能导致网络冲突导致网络异常，这时我们需要重新规划docker 网络，


```
###解除容器绑定的网络 网络名词service_interface_default 容器名称 stable_diffusion_v1
#检查容器使用的网络
docker inspect stable_diffusion_v1  | grep  NetworkMode

#查看主机容器网络
docker network ls
#删除原先的网络
docker network rm service_interface_default
#重新创建容器网络
docker network create --subnet=172.21.0.1/16  service_interface_default
#检查主机路由
route -n

#为容器重新指定网络
docker network connect service_interface_defaultstable_diffusion_v1
#重新启动容器
docker container restart stable_diffusion_v1
```